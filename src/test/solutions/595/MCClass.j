.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()I
Label0:
	bipush 6
	invokestatic MCClass/fac(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iconst_0
	invokestatic MCClass/fac(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iconst_1
	invokestatic MCClass/fac(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iconst_0
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 1
.limit locals 0
.end method

.method public static fac(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpgt Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifeq Label6
Label5:
	iconst_1
	ireturn
	goto Label2
Label6:
Label2:
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MCClass/fac(I)I
	imul
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/Main()I
	pop
Label1:
	return
.limit stack 1
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
