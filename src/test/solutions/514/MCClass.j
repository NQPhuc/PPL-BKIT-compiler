.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x [[Z

.method public static Main()V
Label0:
	getstatic MCClass.x [[Z
	iconst_0
	aaload
	iconst_0
	baload
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	getstatic MCClass.x [[Z
	iconst_1
	aaload
	iconst_1
	baload
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
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
	anewarray [Z
	dup
	iconst_0
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
	aastore
	dup
	iconst_1
	iconst_2
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_1
	bastore
	aastore
	putstatic MCClass.x [[Z
Label1:
	return
.limit stack 7
.limit locals 0
.end method
