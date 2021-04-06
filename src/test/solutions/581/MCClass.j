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
	bipush 100
	istore 4
	iload_0
	iconst_1
	isub
	istore 4
Label6:
	iload 4
	iconst_0
	if_icmplt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifeq Label3
.var 5 is j I from Label4 to Label5
Label4:
	bipush 100
	istore 5
	iload_1
	iconst_1
	isub
	istore 5
Label13:
	iload 5
	iconst_0
	if_icmplt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifeq Label10
.var 6 is k I from Label11 to Label12
Label11:
	bipush 100
	istore 6
	iload_2
	iconst_1
	isub
	istore 6
Label20:
	iload 6
	iconst_0
	if_icmplt Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	ifeq Label17
Label18:
	aload_3
	iload 4
	aaload
	iload 5
	aaload
	iload 6
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label19:
Label16:
	iload 6
	iconst_1
	ineg
	iadd
	istore 6
	goto Label20
Label17:
Label12:
Label9:
	iload 5
	iconst_1
	ineg
	iadd
	istore 5
	goto Label13
Label10:
Label5:
Label2:
	iload 4
	iconst_1
	ineg
	iadd
	istore 4
	goto Label6
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
