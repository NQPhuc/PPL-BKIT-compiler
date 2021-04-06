.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()V
.var 0 is x [[I from Label0 to Label1
Label0:
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iconst_4
	iastore
	aastore
	astore_0
	aload_0
	ldc 1.0
	fneg
	invokestatic io/int_of_float(F)I
	ineg
	aaload
	iconst_1
	ineg
	ineg
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
	return
.limit stack 7
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
