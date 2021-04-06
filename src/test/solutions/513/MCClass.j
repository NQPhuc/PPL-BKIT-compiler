.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [[F

.method public static Main()V
Label0:
	getstatic MCClass.x [[F
	iconst_0
	aaload
	iconst_0
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.x [[F
	iconst_1
	aaload
	iconst_1
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.x [[F
	iconst_2
	aaload
	iconst_2
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
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
	iconst_3
	anewarray [F
	dup
	iconst_0
	iconst_3
	newarray float
	dup
	iconst_0
	ldc 1.1
	fastore
	dup
	iconst_1
	ldc 2.2
	fastore
	dup
	iconst_2
	ldc 3.3
	fastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray float
	dup
	iconst_0
	ldc 4.4
	fastore
	dup
	iconst_1
	ldc 5.5
	fastore
	dup
	iconst_2
	ldc 6.6
	fastore
	aastore
	dup
	iconst_2
	iconst_3
	newarray float
	dup
	iconst_0
	ldc 7.7
	fastore
	dup
	iconst_1
	ldc 8.8
	fastore
	dup
	iconst_2
	ldc 9.9
	fastore
	aastore
	putstatic MCClass.x [[F
Label1:
	return
.limit stack 7
.limit locals 0
.end method
