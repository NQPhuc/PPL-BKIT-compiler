.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()I
.var 0 is iA [I from Label0 to Label1
.var 1 is fA [F from Label0 to Label1
.var 2 is bA [Z from Label0 to Label1
.var 3 is sA [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	bipush 7
	iastore
	astore_0
	iconst_2
	newarray float
	dup
	iconst_0
	ldc 1.3
	fastore
	dup
	iconst_1
	ldc 2.8
	fastore
	astore_1
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	astore_2
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "A"
	aastore
	dup
	iconst_1
	ldc "B"
	aastore
	astore_3
	ldc "iA[0] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_0
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", iA[1] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_0
	iconst_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "bA[0] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_2
	iconst_0
	baload
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", bA[1] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_2
	iconst_1
	baload
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "fA[0] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_0
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", fA[1] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_1
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "sA[0] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_3
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", sA[1] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_3
	iconst_1
	aaload
	invokestatic io/printStrLn(Ljava/lang/String;)V
	aload_0
	iconst_0
	iconst_1
	invokestatic MCClass/swapInt([III)V
	aload_2
	iconst_0
	iconst_1
	invokestatic MCClass/swapBool([ZII)V
	aload_1
	iconst_0
	iconst_1
	invokestatic MCClass/swapFloat([FII)V
	aload_3
	iconst_0
	iconst_1
	invokestatic MCClass/swapString([Ljava/lang/String;II)V
	ldc "iA[0] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_0
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", iA[1] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_0
	iconst_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "bA[0] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_2
	iconst_0
	baload
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", bA[1] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_2
	iconst_1
	baload
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "fA[0] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_0
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", fA[1] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_1
	faload
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "sA[0] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_3
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", sA[1] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_3
	iconst_1
	aaload
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iconst_0
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 4
.limit locals 4
.end method

.method public static swapInt([III)V
.var 0 is x [I from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is temp I from Label0 to Label1
Label0:
	iconst_0
	istore_3
	aload_0
	iload_1
	iaload
	istore_3
	aload_0
	iload_1
	aload_0
	iload_2
	iaload
	iastore
	aload_0
	iload_2
	iload_3
	iastore
	return
Label1:
	return
.limit stack 4
.limit locals 4
.end method

.method public static swapBool([ZII)V
.var 0 is x [Z from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is temp Z from Label0 to Label1
Label0:
	iconst_0
	istore_3
	aload_0
	iload_1
	baload
	istore_3
	aload_0
	iload_1
	aload_0
	iload_2
	baload
	bastore
	aload_0
	iload_2
	iload_3
	bastore
	return
Label1:
	return
.limit stack 4
.limit locals 4
.end method

.method public static swapFloat([FII)V
.var 0 is x [F from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is temp F from Label0 to Label1
Label0:
	ldc 0.0
	fstore_3
	aload_0
	iload_1
	faload
	fstore_3
	aload_0
	iload_1
	aload_0
	iload_2
	faload
	fastore
	aload_0
	iload_2
	fload_3
	fastore
	return
Label1:
	return
.limit stack 4
.limit locals 4
.end method

.method public static swapString([Ljava/lang/String;II)V
.var 0 is x [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is temp Ljava/lang/String; from Label0 to Label1
Label0:
	ldc ""
	astore_3
	aload_0
	iload_1
	aaload
	astore_3
	aload_0
	iload_1
	aload_0
	iload_2
	aaload
	aastore
	aload_0
	iload_2
	aload_3
	aastore
	return
Label1:
	return
.limit stack 4
.limit locals 4
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
