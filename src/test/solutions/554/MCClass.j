.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()V
.var 0 is x Z from Label0 to Label1
.var 1 is y Z from Label0 to Label1
Label0:
	iconst_1
	istore_0
	iconst_0
	istore_1
	iload_0
	ifeq Label2
	iload_0
	ifeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_0
	ifeq Label4
	iload_1
	ifeq Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	ifeq Label6
	iload_0
	ifeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	ifeq Label8
	iload_1
	ifeq Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
