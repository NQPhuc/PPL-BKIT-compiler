.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()I
.var 0 is iA I from Label0 to Label1
.var 1 is iB I from Label0 to Label1
.var 2 is fA F from Label0 to Label1
.var 3 is fB F from Label0 to Label1
.var 4 is bA Z from Label0 to Label1
.var 5 is bB Z from Label0 to Label1
.var 6 is sA Ljava/lang/String; from Label0 to Label1
.var 7 is sB Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	istore_0
	bipush 7
	istore_1
	ldc 1.3
	fstore_2
	ldc 2.8
	fstore_3
	iconst_1
	istore 4
	iconst_0
	istore 5
	ldc "A"
	astore 6
	ldc "B"
	astore 7
	ldc "iA = "
	invokestatic io/print(Ljava/lang/String;)V
	iload_0
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", iB = "
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "bA = "
	invokestatic io/print(Ljava/lang/String;)V
	iload 4
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", bB = "
	invokestatic io/print(Ljava/lang/String;)V
	iload 5
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "fA = "
	invokestatic io/print(Ljava/lang/String;)V
	fload_2
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", fB = "
	invokestatic io/print(Ljava/lang/String;)V
	fload_3
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "sA = "
	invokestatic io/print(Ljava/lang/String;)V
	aload 6
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", sB = "
	invokestatic io/print(Ljava/lang/String;)V
	aload 7
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iload_0
	iload_1
	invokestatic MCClass/swapInt(II)V
	iload 4
	iload 5
	invokestatic MCClass/swapBool(ZZ)V
	fload_2
	fload_3
	invokestatic MCClass/swapFloat(FF)V
	aload 6
	aload 7
	invokestatic MCClass/swapString(Ljava/lang/String;Ljava/lang/String;)V
	ldc "iA = "
	invokestatic io/print(Ljava/lang/String;)V
	iload_0
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", iB = "
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "bA = "
	invokestatic io/print(Ljava/lang/String;)V
	iload 4
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", bB = "
	invokestatic io/print(Ljava/lang/String;)V
	iload 5
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "fA = "
	invokestatic io/print(Ljava/lang/String;)V
	fload_2
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", fB = "
	invokestatic io/print(Ljava/lang/String;)V
	fload_3
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "sA = "
	invokestatic io/print(Ljava/lang/String;)V
	aload 6
	invokestatic io/print(Ljava/lang/String;)V
	ldc ", sB = "
	invokestatic io/print(Ljava/lang/String;)V
	aload 7
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iconst_0
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 2
.limit locals 8
.end method

.method public static swapInt(II)V
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
.var 2 is temp I from Label0 to Label1
Label0:
	iconst_0
	istore_2
	iload_0
	istore_2
	iload_1
	istore_0
	iload_2
	istore_1
	return
Label1:
	return
.limit stack 1
.limit locals 3
.end method

.method public static swapBool(ZZ)V
.var 0 is x Z from Label0 to Label1
.var 1 is y Z from Label0 to Label1
.var 2 is temp Z from Label0 to Label1
Label0:
	iconst_0
	istore_2
	iload_0
	istore_2
	iload_1
	istore_0
	iload_2
	istore_1
	return
Label1:
	return
.limit stack 1
.limit locals 3
.end method

.method public static swapFloat(FF)V
.var 0 is x F from Label0 to Label1
.var 1 is y F from Label0 to Label1
.var 2 is temp F from Label0 to Label1
Label0:
	ldc 0.0
	fstore_2
	fload_0
	fstore_2
	fload_1
	fstore_0
	fload_2
	fstore_1
	return
Label1:
	return
.limit stack 1
.limit locals 3
.end method

.method public static swapString(Ljava/lang/String;Ljava/lang/String;)V
.var 0 is x Ljava/lang/String; from Label0 to Label1
.var 1 is y Ljava/lang/String; from Label0 to Label1
.var 2 is temp Ljava/lang/String; from Label0 to Label1
Label0:
	ldc ""
	astore_2
	aload_0
	astore_2
	aload_1
	astore_0
	aload_2
	astore_1
	return
Label1:
	return
.limit stack 1
.limit locals 3
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
