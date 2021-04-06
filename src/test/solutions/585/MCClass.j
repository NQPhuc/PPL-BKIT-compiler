.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()V
.var 0 is i I from Label0 to Label1
.var 1 is j I from Label0 to Label1
Label0:
	iconst_1
	istore_0
	iconst_1
	istore_1
	iconst_0
	istore_0
Label6:
	iload_0
	bipush 10
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifeq Label3
.var 2 is i I from Label4 to Label5
Label4:
	bipush 7
	istore_2
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iconst_0
	istore_1
Label13:
	iload_1
	iconst_2
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifeq Label10
.var 3 is j I from Label11 to Label12
Label11:
	bipush 8
	istore_3
	iload_3
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label12:
Label9:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label13
Label10:
Label5:
Label2:
	iload_0
	iconst_2
	iadd
	istore_0
	goto Label6
Label3:
	return
Label1:
	return
.limit stack 2
.limit locals 4
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
