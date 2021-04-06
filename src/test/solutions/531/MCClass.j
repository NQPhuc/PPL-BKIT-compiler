.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()V
.var 0 is x [[Ljava/lang/String; from Label0 to Label1
.var 1 is y [[I from Label0 to Label1
Label0:
	iconst_2
	anewarray [Ljava/lang/String;
	dup
	iconst_0
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc "This"
	aastore
	dup
	iconst_1
	ldc " is"
	aastore
	aastore
	dup
	iconst_1
	iconst_2
	anewarray java/lang/String
	dup
	iconst_0
	ldc " a"
	aastore
	dup
	iconst_1
	ldc " random sentence."
	aastore
	aastore
	astore_0
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_2
	newarray int
	dup
	iconst_0
	sipush 200
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	aastore
	dup
	iconst_1
	iconst_2
	newarray int
	dup
	iconst_0
	bipush 6
	iastore
	dup
	iconst_1
	bipush 80
	iastore
	aastore
	astore_1
	aload_0
	iconst_0
	aaload
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	aload_0
	iconst_0
	aaload
	iconst_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	aload_0
	iconst_1
	aaload
	iconst_0
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	aload_0
	iconst_1
	aaload
	iconst_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_0
	aaload
	iconst_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	iconst_1
	aaload
	iconst_0
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
