.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()V
.var 0 is length I from Label0 to Label1
.var 1 is width I from Label0 to Label1
.var 2 is height I from Label0 to Label1
.var 3 is x [[[I from Label0 to Label1
.var 4 is i I from Label0 to Label1
Label0:
	iconst_2
	istore_0
	iconst_3
	istore_1
	iconst_3
	istore_2
	iconst_2
	anewarray [[I
	dup
	iconst_0
	iconst_3
	anewarray [I
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	sipush 200
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	dup
	iconst_2
	bipush 18
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 6
	iastore
	dup
	iconst_1
	bipush 80
	iastore
	dup
	iconst_2
	bipush 79
	iastore
	aastore
	dup
	iconst_2
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 11
	iastore
	dup
	iconst_2
	bipush 12
	iastore
	aastore
	aastore
	dup
	iconst_1
	iconst_3
	anewarray [I
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 9
	iastore
	dup
	iconst_1
	bipush 15
	iastore
	dup
	iconst_2
	bipush 28
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 7
	iastore
	dup
	iconst_1
	bipush 49
	iastore
	dup
	iconst_2
	bipush 60
	iastore
	aastore
	dup
	iconst_2
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 81
	iastore
	dup
	iconst_1
	bipush 16
	iastore
	dup
	iconst_2
	sipush 1024
	iastore
	aastore
	aastore
	astore_3
	iconst_0
	istore 4
.var 5 is j I from Label4 to Label5
Label4:
	iconst_0
	istore 5
	iload 4
	iconst_1
	iadd
	istore 4
.var 6 is k I from Label8 to Label9
Label8:
	iconst_0
	istore 6
	iload 5
	iconst_1
	if_icmpne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifeq Label14
Label13:
	iload 5
	iconst_1
	iadd
	istore 5
	goto Label6
	goto Label10
Label14:
Label10:
	iload 5
	iconst_1
	iadd
	istore 5
Label17:
	iload 6
	iconst_1
	if_icmpne Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifeq Label23
Label22:
	goto Label16
	goto Label19
Label23:
Label19:
	iload 6
	iconst_1
	iadd
	istore 6
	aload_3
	iload 4
	iconst_1
	isub
	aaload
	iload 5
	iconst_1
	isub
	aaload
	iload 6
	iconst_1
	isub
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label18:
Label15:
	iload 6
	iload_2
	if_icmpge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifne Label17
Label16:
Label9:
Label6:
	iload 5
	iload_1
	if_icmpge Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifne Label8
Label7:
Label5:
Label2:
	iload 4
	iload_0
	if_icmpge Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	ifne Label4
Label3:
	return
Label1:
	return
.limit stack 10
.limit locals 7
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/Main()V
Label1:
	return
.limit stack 0
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
