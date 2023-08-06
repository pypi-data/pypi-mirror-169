# OSACA-BEGIN
.L19:
	vmovupd	(%r14,%rsi), %ymm14
	vfmadd213pd	(%r13,%rsi), %ymm6, %ymm14
	vmovupd	%ymm14, (%r12,%rsi)
	addq	$32, %rsi
	cmpq	%rsi, %rcx
	jne	.L19
# OSACA-END
