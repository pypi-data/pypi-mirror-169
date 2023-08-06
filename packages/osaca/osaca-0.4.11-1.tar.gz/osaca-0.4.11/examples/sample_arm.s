sub sp, sp, #16 
str w0, [sp, #12]
ldr w8, [sp, #12]
mul w0, w8, w9
ret
sub sp, sp, #112
stp x29, x30, [sp, #16]
b.lt .LBB0_13
sub x6, x11, #2    
mov w10, w2
lsl x1, x10, #1
cmp x6, #1 
sub x19, x1, #2
and x6, x6, #0xfffffffffffffffe
dup v1.2d, v0.d[0]
and w21, w1, w21
b .LBB0_4
b.eq .LBB0_13
b.hs .LBB0_10
mov w1, #2
mul x24, x18, x1
sub x27, x11, x1
subs x27, x27, #1
