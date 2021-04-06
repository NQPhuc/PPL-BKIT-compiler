.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I
.field static d I

.method public static Main()V
.var 0 is matrix [[I from Label0 to Label1
Label0:
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	aastore
	astore_0
	ldc "Creating 2x2 matrix:\n"
	invokestatic io/print(Ljava/lang/String;)V
	ldc "a\tb\nc\td\n"
	invokestatic io/print(Ljava/lang/String;)V
	ldc "a = "
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.a I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "b = "
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.b I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "c = "
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.c I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "d = "
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.d I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass.a I
	getstatic MCClass.b I
	getstatic MCClass.c I
	getstatic MCClass.d I
	invokestatic MCClass/matrix_2x2(IIII)[[I
	astore_0
	ldc "m[0][0] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_0
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "m[0][1] = "
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.a I
	getstatic MCClass.b I
	getstatic MCClass.c I
	getstatic MCClass.d I
	invokestatic MCClass/matrix_2x2(IIII)[[I
	iconst_0
	aaload
	iconst_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "m[1][0] = "
	invokestatic io/print(Ljava/lang/String;)V
	aload_0
	iconst_1
	aaload
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	ldc "m[1][1] = "
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.a I
	getstatic MCClass.b I
	getstatic MCClass.c I
	getstatic MCClass.d I
	invokestatic MCClass/matrix_2x2(IIII)[[I
	iconst_1
	aaload
	iconst_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
	return
.limit stack 7
.limit locals 1
.end method

.method public static matrix_2x2(IIII)[[I
.var 0 is a00 I from Label0 to Label1
.var 1 is a01 I from Label0 to Label1
.var 2 is a10 I from Label0 to Label1
.var 3 is a11 I from Label0 to Label1
.var 4 is m [[I from Label0 to Label1
Label0:
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	aastore
	astore 4
	aload 4
	iconst_0
	aaload
	iconst_0
	iload_0
	iastore
	aload 4
	iconst_0
	aaload
	iconst_1
	iload_1
	iastore
	aload 4
	iconst_1
	aaload
	iconst_0
	iload_2
	iastore
	aload 4
	iconst_1
	aaload
	iconst_1
	iload_3
	iastore
	aload 4
	areturn
Label1:
	iconst_1
	anewarray [I
	areturn
.limit stack 7
.limit locals 5
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
	putstatic MCClass.a I
	iconst_4
	putstatic MCClass.b I
	iconst_5
	putstatic MCClass.c I
	bipush 6
	putstatic MCClass.d I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
