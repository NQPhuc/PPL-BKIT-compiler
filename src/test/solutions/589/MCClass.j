.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I
.field static j I

.method public static Main()V
Label0:
Label2:
	getstatic MCClass.i I
	bipush 10
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifeq Label3
.var 0 is i I from Label4 to Label5
Label4:
	bipush 6
	istore_0
	iload_0
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label8:
	getstatic MCClass.j I
	iconst_2
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifeq Label9
.var 1 is j I from Label10 to Label11
Label10:
	bipush 8
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iconst_1
	invokestatic MCClass/jIncrease(I)V
Label11:
	goto Label8
Label9:
	iconst_2
	invokestatic MCClass/iIncrease(I)V
	iconst_0
	putstatic MCClass.j I
Label5:
	goto Label2
Label3:
	return
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static iIncrease(I)V
.var 0 is n I from Label0 to Label1
Label0:
	getstatic MCClass.i I
	iload_0
	iadd
	putstatic MCClass.i I
	return
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static jIncrease(I)V
.var 0 is n I from Label0 to Label1
Label0:
	getstatic MCClass.j I
	iload_0
	iadd
	putstatic MCClass.j I
	return
Label1:
	return
.limit stack 2
.limit locals 1
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
	iconst_0
	putstatic MCClass.i I
	iconst_0
	putstatic MCClass.j I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
