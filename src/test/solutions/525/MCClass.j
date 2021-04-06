.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()V
.var 0 is x [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "aaa"
	aastore
	dup
	iconst_1
	ldc "bbb"
	aastore
	astore_0
	aload_0
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	aload_0
	iconst_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
	return
.limit stack 4
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
