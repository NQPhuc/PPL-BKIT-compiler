.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()V
.var 0 is x Z from Label0 to Label1
Label0:
	iconst_1
	istore_0
	iload_0
	ifne Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifeq Label6
Label5:
	ldc "1"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label6:
Label7:
	ldc "2"
	invokestatic io/print(Ljava/lang/String;)V
Label8:
Label2:
	return
Label1:
	return
.limit stack 1
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
