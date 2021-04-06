.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()V
Label0:
	invokestatic MCClass/foo2()Z
	ifeq Label4
	invokestatic MCClass/foo()Z
	ifeq Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifne Label2
	invokestatic MCClass/foo()Z
	ifeq Label6
	invokestatic MCClass/foo2()Z
	ifeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifne Label2
	iconst_0
	goto Label3
Label2:
	iconst_1
Label3:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public static foo()Z
Label0:
	ldc "foo(),"
	invokestatic io/print(Ljava/lang/String;)V
	iconst_1
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 1
.limit locals 0
.end method

.method public static foo2()Z
Label0:
	ldc "foo2(),"
	invokestatic io/print(Ljava/lang/String;)V
	iconst_0
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
