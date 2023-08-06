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

!*****************************************************!
!*          SEISCOPE OPTIMIZATION TOOLBOX            *!
!*****************************************************!
! This program provides an example for using the      !
! preconditioned truncated Newton algorithm within the!
! SEISCOPE OPTIMIZATION TOOLBOX.                      !
!                                                     !
! The algorithm implemented is described in           !
! L.Metivier, R. Brossier, J. Virieux, S.Operto,      !
! Truncated Newton and full waveform inversion, 2013  !
! SIAM Journal on Scientific Computing, Vol. 35,      !
! No. 2, pp. B401–B437,                               !         
!                                                     !
! The 2D Rosenbrock function is minimized             !
! f(x,y)  = (1-x)**2+100.*(y-x**2)**2                 !
!                                                     !
! The computation of this function and its gradient   !
! is implemented in                                   !
! ../../../COMMON/test/rosenbrock.f90                 !
! routine rosenbrock                                  !
!                                                     !
! The preconditioned truncated Newton method also     !
! requires to compute Hessian-vector products. This   !
! is implemented in                                   ! 
! ../../../COMMON/test/rosenbrock.f90                 !
! routine rosenbrok_hess                              !
!                                                     !
! The communication with the PTRN optimizer is        ! 
! achieved through the variable FLAG. The only        !
! difference with the TRN optimizer is that a         !
! preconditioner can be used to improve the           !
! convergence speed of the inner conjugate gradient   !
! iterations. This preconditioner is applied to the   !
! gradient, and to the residual of the inner linear   !
! system.  
!                                                     !
! Here are the actions requested for the user         !
! 1. Before first call, the user must set the         !
!    optimization parameters, namely                  !
!    - maximum number of iterations optim%niter_max   !
!    - tolerance for the stopping criterion           !
!      optim%conv                                     !
!      (this stopping criterion is the default one    !
!        in the TOOLBOX and is based on the decrease  !
!        of the misfit function scaled to one at the  !
!        first iteration)                             !
!     - level of details in the output                !
!       * if optim%debug=.true. then the information  !
!         on the linesearch process is provided       !
!         additional information related to the       !
!         quadratic function minimized throughout the !
!         inner conjugate gradient iterations is also !
!         provided as a quality control               !
!       * if optim%debug=.false. a more compact output!
!         file is provided                            !
!   - initialize x with an arbitrary initial guess    !
!   - initialize fcost with the cost function         !
!     associated with the initial guess               !
!   - initialize grad with the gradient associated    !
!     with the initial guess                          !
!   - initialize grad_preco with the gradient         !
!     associated with the initial guess multiplied by !
!     the preconditioner                              !
! 2. On first call, FLAG must be set to INIT          !
! 3. When the FLAG returned by PTRN is 'GRAD', then   !
!    the user must compute the cost, the gradient     !
!    and the preconditioned gradient at current       !
!    iterate x in fcost, grad, grad_preco             !
! 4. When the FLAG returned by PTRN is 'PREC', then   !
!    multiply the vector optim%residual by the        !
!    preconditioner and store the result in           !
!    optim%residual_preco                             !
! 5. When the FLAG returned by PTRN is 'HESS', then   !
!    multiply the vector optim%d by the Hessian       !
!    and store the result in optim%Hd                 ! 
!-----------------------------------------------------!
program test_PTRN
  !use typedef
  !use opt_PTRN
  use seiscope_optimization_toolbox
  implicit none  
  
  integer :: n                                ! dimension of the problem
  real :: fcost                               ! cost function value
  real,dimension(:),allocatable :: x          ! current point
  real,dimension(:),allocatable :: grad       ! current gradient
  real,dimension(:),allocatable :: grad_preco ! preconditioned current gradient
  real,dimension(:),allocatable :: d, Hd
  real,dimension(:),allocatable :: residual,residual_preco
  type(optim_type) :: optim                   ! data structure for the optimizer
  !character*4 :: FLAG                         ! communication FLAG 
  integer :: FLAG                             ! communication FLAG
  

  !----------------------------------------------------!
  ! Set size of one-dimensional solution array and     !
  ! first flag value                                   !
  !----------------------------------------------------!
  n=2     ! dimension
  FLAG=0  ! first flag -- 'INIT' in original version
  
  !----------------------------------------------------!
  ! intial guess                                       !
  !----------------------------------------------------!
  allocate(x(n),grad(n),grad_preco(n),d(n),Hd(n))
  allocate(residual(n),residual_preco(n))
  x(1)=1.5
  x(2)=1.5
  
  !----------------------------------------------------!
  ! computation of the cost and gradient associated    !
  ! with the initial guess                             !
  !----------------------------------------------------!
  call Rosenbrock(x,fcost,grad)

  !----------------------------------------------------!
  ! multiplication of the gradient by the              !
  ! preconditioner (here preconditioner is identity:   !
  ! no preconditioning)                                !
  !----------------------------------------------------!
  grad_preco(:)=grad(:)  
  
  !----------------------------------------------------!
  ! parameter initialization (i.e., maximum iteration  !
  ! number, tolerance for stopping criterion, print    !
  ! info in output files, etc)                         !
  !----------------------------------------------------!
  call set_inputs(optim, fcost, 100, 1., 20, 1e-8, &
                  l=20, niter_max_CG=5)
                  
  !----------------------------------------------------!
  ! optimization loop: while convergence not reached or!
  ! linesearch not failed, iterate                     !
  !----------------------------------------------------!
  !do while ((FLAG.ne.'CONV').and.(FLAG.ne.'FAIL'))
  do while ((FLAG.ne.2).and.(FLAG.ne.4)) 
     call PTRN(n,x,fcost,grad,grad_preco,residual,residual_preco, &
               d,Hd,optim,FLAG)
     !if(FLAG.eq.'GRAD') then   
     if(FLAG.eq. 1) then                   
        !----------------------------------------------------!
        ! if FLAG is GRAD, then compute cost, gradient and   !
        ! preconditioned gradient in fcost, grad, grad_preco !
        !----------------------------------------------------!
        call Rosenbrock(x,fcost,grad)        
        grad_preco(:)=grad(:)
     !elseif(FLAG.eq.'HESS') then
     elseif(FLAG.eq. 7) then
        !----------------------------------------------------!
        ! if FLAG is HESS, then multiply optim%d by the      !
        ! Hessian operator and store the result in optim%Hd  !
        !----------------------------------------------------!
        call Rosenbrock_Hess(x,d,Hd)
     !elseif(FLAG.eq.'PREC') then
     elseif(FLAG.eq. 8) then
        !----------------------------------------------------!
        ! if FLAG is PREC, then multiply optim%residual by   !
        ! preconditioner and store the result in             !
        ! optim%residual_preco                               !
        !----------------------------------------------------!
        residual_preco(:)=residual(:)
     endif
  enddo
  
  !Helpful console writings
  write(*,*) 'END OF TEST'
  write(*,*) 'FINAL iterate is : ', x(:)
  write(*,*) 'See the convergence history in iterate_PTRN.dat and iterate_PTRN_CG.dat'
  
end program test_PTRN

