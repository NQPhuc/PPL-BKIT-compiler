.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x I
.field static y F
.field static s Ljava/lang/String;
.field static z I
.field static b Z

.method public static Main()V
Label0:
	getstatic MCClass.x I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass.y F
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass.z I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass.s Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	getstatic MCClass.b Z
	invokestatic io/string_of_bool(Z)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
	return
.limit stack 1
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
	bipush 100
	putstatic MCClass.x I
	ldc 1.0
	putstatic MCClass.y F
	ldc "Phuc"
	putstatic MCClass.s Ljava/lang/String;
	iconst_5
	putstatic MCClass.z I
	iconst_1
	putstatic MCClass.b Z
Label1:
	return
.limit stack 1
.limit locals 0
.end method
