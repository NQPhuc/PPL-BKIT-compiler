.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()V
.var 0 is x Z from Label0 to Label1
Label0:
	iconst_0
	istore_0
	invokestatic MCClass/foo()Z
	ifeq Label2
	iload_0
	ifeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_0
	ifeq Label4
	invokestatic MCClass/foo()Z
	ifeq Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static foo()Z
Label0:
	ldc "TEST"
	invokestatic io/print(Ljava/lang/String;)V
	iconst_1
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 1
.limit locals 0
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
