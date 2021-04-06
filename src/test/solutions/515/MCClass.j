.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [[Ljava/lang/String;

.method public static Main()V
Label0:
	getstatic MCClass.x [[Ljava/lang/String;
	iconst_0
	aaload
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.x [[Ljava/lang/String;
	iconst_0
	aaload
	iconst_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.x [[Ljava/lang/String;
	iconst_1
	aaload
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.x [[Ljava/lang/String;
	iconst_1
	aaload
	iconst_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
	return
.limit stack 2
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
	iconst_2
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "This"
	aastore
	dup
	iconst_1
	ldc " is"
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc " a"
	aastore
	dup
	iconst_1
	ldc " random sentence."
	aastore
	aastore
	putstatic MCClass.x [[Ljava/lang/String;
Label1:
	return
.limit stack 7
.limit locals 0
.end method
