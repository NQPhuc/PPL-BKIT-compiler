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
	ldc "a^b = "
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.a I
	getstatic MCClass.b I
	invokestatic MCClass/power(II)I
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

.method public static power(II)I
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
.var 2 is r I from Label0 to Label1
.var 3 is i I from Label0 to Label1
Label0:
	iconst_1
	istore_2
	iconst_0
	istore_3
	iconst_0
	istore_3
Label6:
	iload_3
	iload_1
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifeq Label3
Label4:
	iload_2
	iload_0
	imul
	istore_2
Label5:
Label2:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label6
Label3:
	iload_2
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 2
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
	iconst_3
	putstatic MCClass.a I
	iconst_4
	putstatic MCClass.b I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
