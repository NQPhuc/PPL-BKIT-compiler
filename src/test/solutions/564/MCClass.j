.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()V
.var 0 is x Z from Label0 to Label1
Label0:
	iconst_0
	istore_0
	bipush 7
	ineg
	invokestatic io/float_to_int(I)F
	ldc 7.5
	fneg
	fcmpl
	ifle Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	bipush 7
	ineg
	invokestatic io/float_to_int(I)F
	ldc 7.5
	fneg
	fcmpl
	ifge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifne Label8
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
.limit stack 2
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
