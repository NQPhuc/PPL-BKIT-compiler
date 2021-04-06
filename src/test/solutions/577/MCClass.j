.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()V
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
	iconst_3
	istore_0
	iconst_2
	istore_1
	iload_0
	iconst_1
	if_icmpne Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifeq Label6
.var 2 is x I from Label5 to Label6
Label5:
	iconst_2
	istore_2
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_2
	iconst_2
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifeq Label11
Label10:
	ldc "A"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label7
Label11:
Label7:
	goto Label2
Label6:
.var 2 is y I from Label12 to Label13
Label12:
	iconst_3
	istore_2
	iload_2
	iconst_2
	if_icmpne Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifeq Label18
Label17:
	ldc "B"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label14
Label18:
Label19:
	ldc "C"
	invokestatic io/print(Ljava/lang/String;)V
Label20:
Label14:
	ldc "abc"
	invokestatic io/print(Ljava/lang/String;)V
Label13:
Label2:
	return
Label1:
	return
.limit stack 2
.limit locals 3
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
