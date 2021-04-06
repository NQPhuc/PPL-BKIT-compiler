.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b I

.method public static Main()I
Label0:
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
	ldc "a + b = "
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.a I
	getstatic MCClass.b I
	invokestatic MCClass/sum(II)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iconst_0
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 2
.limit locals 0
.end method

.method public static sum(II)I
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 2
.limit locals 2
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
	bipush 81
	putstatic MCClass.a I
	bipush 67
	putstatic MCClass.b I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
