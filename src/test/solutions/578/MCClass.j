.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Main()V
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
	iconst_1
	istore_0
	iconst_2
	istore_1
	iload_0
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
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
.var 3 is x I from Label10 to Label11
Label10:
	iconst_3
	istore_3
	iload_3
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_3
	iconst_3
	if_icmpne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifeq Label16
.var 4 is x I from Label15 to Label16
Label15:
	iconst_4
	istore 4
	iload 4
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label12
Label16:
Label12:
	goto Label7
Label11:
Label7:
	goto Label2
Label6:
Label2:
	return
Label1:
	return
.limit stack 2
.limit locals 5
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
