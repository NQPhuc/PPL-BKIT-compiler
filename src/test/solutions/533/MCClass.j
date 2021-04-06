.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x Ljava/lang/String;

.method public static Main()V
.var 0 is y I from Label0 to Label1
.var 1 is x F from Label0 to Label1
Label0:
	iconst_1
	istore_0
	ldc 5.7
	fstore_1
	iload_0
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	fload_1
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
	return
.limit stack 1
.limit locals 2
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
	ldc "Local var"
	putstatic MCClass.x Ljava/lang/String;
Label1:
	return
.limit stack 1
.limit locals 0
.end method
