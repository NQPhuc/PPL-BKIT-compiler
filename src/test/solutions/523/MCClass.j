.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()V
.var 0 is x [F from Label0 to Label1
Label0:
	iconst_3
	newarray float
	dup
	iconst_0
	ldc 0.01
	fastore
	dup
	iconst_1
	ldc 2.0
	fastore
	dup
	iconst_2
	ldc 38000000.0
	fastore
	astore_0
	aload_0
	iconst_0
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	aload_0
	iconst_1
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	aload_0
	iconst_2
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
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
