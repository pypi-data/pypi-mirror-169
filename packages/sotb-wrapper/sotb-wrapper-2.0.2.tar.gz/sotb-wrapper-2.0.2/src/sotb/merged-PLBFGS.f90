!******************************************************************
!Copyright 2013-2016 SEISCOPE II project, All rights reserved.
!
!Redistribution and use in source and binary forms, with or
!without modification, are permitted provided that the following
!conditions are met:
!
!    *  Redistributions of source code must retain the above copyright
!       notice, this list of conditions and the following disclaimer.
!    *  Redistributions in binary form must reproduce the above
!       copyright notice, this list of conditions and the following
!       disclaimer in the documentation and/or other materials provided
!       with the distribution.
!    *  Neither the name of the SEISCOPE project nor the names of
!       its contributors may be used to endorse or promote products
!       derived from this software without specific prior written permission.
!
!Warranty Disclaimer:
!THIS SOFTWARE IS PROVIDED BY THE SEISCOPE PROJECT AND CONTRIBUTORS
!"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
!LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
!FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
!SEISCOPE PROJECT OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
!INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
!BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
!LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
!CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
!STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
!IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
!POSSIBILITY OF SUCH DAMAGE.

module opt_PLBFGS
use, intrinsic :: iso_c_binding
use typedef
use miscellaneous
use opt_PSTD, only : xk, descent
use opt_LBFGS, only : save_LBFGS, update_LBFGS, sk, yk

private
real, allocatable, dimension(:) :: alpha_plb,rho_plb
public PLBFGS

contains

subroutine plbfgs_centry(n,x,fcost,grad,grad_preco,q_plb,optim,flag,lb,ub) bind(c, name='PLBFGS')
  !IN
  integer(c_int), value  :: n                    !dimension of the problem
  real(c_float)   :: fcost                       !cost associated with x
  real(c_float),dimension(n) :: grad,grad_preco !gradient and preconditioned gradient at x 
  real(c_float),dimension(n) :: q_plb
  !IN/OUT  
  integer(c_int)  :: flag
  real(c_float),dimension(n) :: x               !current point
  type(optim_type) :: optim            !data structure 
  type(c_ptr), value  :: lb,ub
  real(c_float), pointer, dimension(:) :: lb_pass, ub_pass

  nullify(lb_pass)
  nullify(ub_pass)
  if (c_associated(ub)) call c_f_pointer(ub, ub_pass, (/n/))
  if (c_associated(lb)) call c_f_pointer(lb, lb_pass, (/n/))
  call plbfgs(n,x,fcost,grad,grad_preco,q_plb,optim,flag,lb_pass,ub_pass)
end subroutine plbfgs_centry

!*****************************************************!
!*          SEISCOPE OPTIMIZATION TOOLBOX            *!
!*****************************************************!
! This file contains the two parts of the computation !
! of the l-BFGS descent direction following the two   !
! recursion loop algorithm                            ! 
! Nocedal, 2nd edition, 2006 Algorithm 7.5 p. 179     !
! Basically, the two loops have been split, compared  !
! to the standard l-BFGS algorithm, to allow the user !
! to use its preconditioner as an initial estimation  !
! of the inverse Hessian operator                     ! 
!-----------------------------------------------------!

!-----------------------------------------------------!
!FIRST LOOP: descent1_PLBFGS                          !
!------------------------------------------------------
! INPUT : integer n dimension                         !
!         real,dimension(n) grad current gradient     !
!         real,dimension(n,l) sk yk pairs of vectors  !
!                             for l-BFGS approximation!
!         integer cpt_lbfgs current number of stored  !
!                           pairs                     !
!         integer l maximum number of stored pairs    !
! OUTPUT : real,dimension(n) descent                  !
!-----------------------------------------------------!
subroutine descent1_PLBFGS(n,grad,sk,yk,cpt_lbfgs,l,q_plb)
  
  implicit none

  !IN
  integer :: n,cpt_lbfgs,l
  real,dimension(n) :: grad, q_plb
  real,dimension(n,l) :: sk,yk
  !Local variables
  integer :: i,borne_i
  
  borne_i=cpt_lbfgs-1
  allocate(alpha_plb(cpt_lbfgs))
  allocate(rho_plb(cpt_lbfgs))  
  q_plb(:)=grad(:)
  do i=1,borne_i
     rho_plb(borne_i-i+1)= dot_product(yk(:,borne_i-i+1),sk(:,borne_i-i+1))
     rho_plb(borne_i-i+1)=1./rho_plb(borne_i-i+1)
     alpha_plb(borne_i-i+1)= dot_product (sk(:,borne_i-i+1),q_plb(:))
     alpha_plb(borne_i-i+1)=rho_plb(borne_i-i+1)*alpha_plb(borne_i-i+1)
     q_plb(:)=q_plb(:)-alpha_plb(borne_i-i+1)*yk(:,borne_i-i+1)
  enddo
  
end subroutine descent1_PLBFGS

!-----------------------------------------------------!
!SECOND LOOP: descent2_PLBFGS                         !
!------------------------------------------------------
! INPUT : integer n dimension                         !
!         real,dimension(n) grad current gradient     !
!         real,dimension(n,l) sk yk pairs of vectors  !
!                             for l-BFGS approximation!
!         integer cpt_lbfgs current number of stored  !
!                           pairs                     !
!         integer l maximum number of stored pairs    !
! OUTPUT : real,dimension(n) descent                  !
!-----------------------------------------------------!
subroutine descent2_PLBFGS(n,sk,yk,cpt_lbfgs,l,descent,q_plb)
  
  implicit none
  
  !IN
  integer :: n,cpt_lbfgs,l
  real,dimension(n,l) :: sk,yk
  !IN/OUT
  real,dimension(n) :: descent, q_plb
  !Local variables
  real :: beta,gamma,gamma_num,gamma_den
  integer :: i,borne_i
  
  borne_i=cpt_lbfgs-1  
  gamma_num = dot_product(sk(:,borne_i),yk(:,borne_i))
  gamma_den = norm2 (yk(:,borne_i))
  gamma=gamma_num/(gamma_den**2)     
  descent(:)=gamma*q_plb(:)
  do i=1,borne_i
     beta = dot_product(yk(:,i),descent(:))
     beta= rho_plb(i)*beta
     descent(:)=descent(:)+(alpha_plb(i)-beta)*sk(:,i)
  enddo
  descent(:)=-1.*descent(:)
  deallocate(alpha_plb,rho_plb)
  
end subroutine descent2_PLBFGS
!*********************************************!
!*    SEISCOPE OPTIMIZATION TOOLBOX          *!
!*********************************************!
! This routine is used to deallocate all the  !
! arrays that have been used during the       !
! PSTD optimization                           !
!---------------------------------------------!
! INPUT/OUT:  optim_type optim                !
!---------------------------------------------!
subroutine finalize_PLBFGS()
  
  implicit none 
  
  deallocate(xk)
  deallocate(descent)
  deallocate(sk)
  deallocate(yk)  
  
end subroutine finalize_PLBFGS

!*****************************************************!
!*          SEISCOPE OPTIMIZATION TOOLBOX            *!
!*****************************************************!
! This routine is the reverse communication mode      !
! preconditioned l-BFGS algorithm. This algorithm is  !
! described in :                                      !
! Numerical Optimization, Nocedal, 2nd edition, 2006  !
! Algorithm 7.4 p. 178, Algorithm 7.5 p. 179          !
!                                                     !
! This routine performs an iterative                  !
! minimization of a function f following the          !
! recurrence                                          !
!                                                     !
! x_{0}=x0                                            !
! x_{k+1}=x_k+\alpha_k d_k                            !
!                                                     !
! where the descent direction d_k is                  !
!                                                     !
! d_k=-Q_k \nabla f_k                                 !
!                                                     !
! with Q_k        : l-BFGS approximation of the       !
!                   inverse Hessian at iteration k    !
!                   including preconditioning info    !
!\nabla f_k       : gradient of f in x_k              !
!                                                     !
! and alpha_k is the steplength computed through the  !
! common linesearch algorithm of the TOOLBOX          !
!                                                     !
! The only difference with the l-BFGS algorithm is in !
! the computation of the descent direction d_k which  !
! can now include a prior information on the inverse  !
! hessian operator.                                   !
!                                                     !
! The first call to the algorithm must be done with   !
! FLAG='INIT'. For this first call, the initial point !
! x0 is given through the variable x, and the input   !
! variable fcost and grad must correspond respectively!
! to the misfit and gradient at x0.                   !
!                                                     !
! The reverse communication with the user is          !
! performed through the variable FLAG. This           !
! variable indicates to the user on return what action! 
! he has to do, or the state of the algorithm.        !
! Possible values are                                 !
! - FLAG='GRAD' => the user must compute the cost and !
!                  (preconditioned) gradient at       !
!                  current point x                    !
! - FLAG='PREC' => the user must multiply the vector   !
!                  optim%q_plb by its preconditioner  !
! - FLAG='CONV' => a minimizer has been found         !
! - FLAG='NSTE' => a new step is performed            !
! - FLAG='FAIL' => the linesearch has failed          !
!-----------------------------------------------------!
! INPUT  : integer :: n (dimension)                   ! 
!          real fcost (current cost)                  !
!          real,dimension(n) grad                     !
!          real,dimension(n) grad_preco               !
! INPUT/OUTPUT : real,dimension(n) x                  !
!                optim_typ optim (data structure)     !
!                character*4 FLAG (communication)     !
!-----------------------------------------------------!
subroutine PLBFGS(n,x,fcost,grad,grad_preco,q_plb,optim,flag,lb,ub)
  
  implicit none
  
  !IN
  integer  :: n                            !dimension of the problem
  real :: fcost                          !cost associated with x
  real,dimension(n) :: grad              !associated gradient 
  real,dimension(n) :: grad_preco        !preconditioned gradient (first iteration only) 
  real,dimension(n) :: q_plb
  !IN/OUT  
  integer  :: flag
  real,dimension(n) :: x          !current point
  type(optim_type) :: optim                !data structure
  real(c_float),optional, dimension(n) :: lb,ub 
  !Local variables
  logical :: test_conv
  
  if(FLAG.eq. 0) then
     !-----------------------------------------------------!
     ! if FLAG is INIT, call the dedicated initialization  !
     ! subroutine to allocate data structure optim and     !
     ! initialize the linesearch process                   !
     !-----------------------------------------------------!
     !call init_PLBFGS(n,optim%l,x,fcost,grad,grad_preco,optim)
     allocate(sk(n,optim%l), yk(n,optim%l), xk(n), descent(n))
     sk(:,:)=0.
     yk(:,:)=0.
     xk(:)=x(:)
     descent(:)=-1.*grad_preco(:)
     call save_LBFGS(n,optim%cpt_lbfgs,optim%l,x,grad,sk,yk)
     call std_linesearch(n,x,fcost,grad,xk,descent,optim,lb,ub)
     call print_info(n,'PL',optim,fcost,grad,FLAG)
     FLAG=1     
     optim%nfwd_pb=optim%nfwd_pb+1
  elseif(FLAG.eq. 5) then
     !-----------------------------------------------------!
     ! if FLAG is PREC, we return from a call to the       !
     ! user preconditioner, then we have to finish the     !
     ! computation of the descent direction                !
     !-----------------------------------------------------!
     call descent2_PLBFGS(n,sk,yk,optim%cpt_lbfgs,&
          optim%l,descent,q_plb)         
     !LBFGS save
     call save_LBFGS(n,optim%cpt_lbfgs,optim%l,x,grad,sk,yk)
     optim%cpt_iter=optim%cpt_iter+1        
     !-----------------------------------------------------!
     ! before continuing we test for convergence           !
     !-----------------------------------------------------!
     call std_test_conv(optim,fcost,test_conv)
     if(test_conv) then
        FLAG=2
        !print info on current iteration
        call print_info(n,'PL',optim,fcost,grad,FLAG)
        call finalize_PLBFGS
     else
        FLAG=3
        !print info on current iteration
        call print_info(n,'PL',optim,fcost,grad,FLAG)
     endif
  else
     !-----------------------------------------------------!
     ! else call the linesearch process                    !  
     !-----------------------------------------------------!
     call std_linesearch(n,x,fcost,grad,xk,descent,optim,lb,ub)     
     if(optim%task.eq. 0) then 
        !LBFGS update        
        call update_LBFGS(n,optim%cpt_lbfgs,optim%l,x,grad,sk,yk)
        !Start the computation of the new descent direction
        call descent1_PLBFGS(n,grad,sk,yk,optim%cpt_lbfgs,optim%l,q_plb)         
        !Set FLAG to PREC for asking user to perform preconditioning 
        FLAG=5                        
     elseif(optim%task.eq. 1) then 
        !-----------------------------------------------------!
        ! if the linesearch needs a new gradient then ask the !  
        ! user to provide it
        !-----------------------------------------------------!
        FLAG=1
        optim%nfwd_pb=optim%nfwd_pb+1
     elseif(optim%task.eq. 2) then        
        !-----------------------------------------------------!
        ! if the linesearch has failed, inform the user       !
        !-----------------------------------------------------!
        FLAG=4
        !print info on current iteration
        call print_info(n,'PL',optim,fcost,grad,FLAG)
        call finalize_PLBFGS
     endif
  endif
  
end subroutine PLBFGS

end module opt_PLBFGS

