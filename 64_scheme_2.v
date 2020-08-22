`timescale 1ns/1ps

module approx_multiplier_1 (input [63:0]a, input [63:0]b, output reg [127:0]y);
integer i,j,k,l,sum1,sum2,sum,num;
reg [9:0]m;   // m and n are the two partial numbers 
reg [9:0]n;

always @(a or b)
begin

if (a[63] || a[62] || b[63] || b[62] )
begin
num=10;
end

else if (a[61] || a[60] || a[59] || a[58] || b[61] || b[60] || b[59] || b[58])
begin
num=9;
end

else if (a[57] || a[56] || a[55] || b[57] || b[56] || b[55])
begin
num=8;
end

else
begin
num=7;
end



if (a[63]==1)
begin
k=63;
end
else if(a[62]==1)
begin
k=62;
end

else if(a[61]==1)
begin
k=61;
end

else if(a[60]==1)
begin
k=60;
end

else if(a[59]==1)
begin
k=59;
end

else if(a[58]==1)
begin
k=58;
end
else if (a[57]==1)
begin
k=57;
end
else if(a[56]==1)
begin
k=56;
end

else if(a[55]==1)
begin
k=55;
end

else if(a[54]==1)
begin
k=54;
end

else if(a[53]==1)
begin
k=53;
end

else if(a[52]==1)
begin
k=52;
end

else if(a[51]==1)
begin
k=51;
end

else if(a[50]==1)
begin
k=50;
end

else if(a[49]==1)
begin
k=49;
end
else if(a[48]==1)
begin
k=48;
end
else if(a[47]==1)
begin
k=47;
end
else if(a[46]==1)
begin
k=46;
end
else if(a[45]==1)
begin
k=45;
end

else if(a[44]==1)
begin
k=44;
end

else if(a[43]==1)
begin
k=43;
end

else if(a[42]==1)
begin
k=42;
end

else if(a[41]==1)
begin
k=41;
end

else if(a[40]==1)
begin
k=40;
end

else if(a[39]==1)
begin
k=39;
end

else if(a[38]==1)
begin
k=38;
end

else if(a[37]==1)
begin
k=37;
end

else if(a[36]==1)
begin
k=36;
end


else if(a[35]==1)
begin
k=35;
end

else if(a[34]==1)
begin
k=34;
end

else if(a[33]==1)
begin
k=33;
end
else if (a[32]==1)
begin
k=32;
end

else if(a[31]==1)
begin
k=31;
end

else if(a[30]==1)
begin
k=30;
end

else if(a[29]==1)
begin
k=29;
end

else if(a[28]==1)
begin
k=28;
end

else if(a[27]==1)
begin
k=27;
end

else if(a[26]==1)
begin
k=26;
end
else if (a[25]==1)
begin
k=25;
end
else if(a[24]==1)
begin
k=24;
end

else if(a[23]==1)
begin
k=23;
end

else if(a[22]==1)
begin
k=22;
end

else if(a[21]==1)
begin
k=21;
end

else if(a[20]==1)
begin
k=20;
end

else if(a[19]==1)
begin
k=19;
end

else if(a[18]==1)
begin
k=18;
end

else if(a[17]==1)
begin
k=17;
end
else if(a[16]==1)
begin
k=16;
end
else if(a[15]==1)
begin
k=15;
end
else if(a[14]==1)
begin
k=14;
end
else if(a[13]==1)
begin
k=13;
end

else if(a[12]==1)
begin
k=12;
end

else if(a[11]==1)
begin
k=11;
end

else if(a[10]==1)
begin
k=10;
end

else if(a[9]==1)
begin
k=9;
end

else if(a[8]==1)
begin
k=8;
end

else if(a[7]==1)
begin
k=7;
end

else if(a[6]==1)
begin
k=6;
end

else if(a[5]==1)
begin
k=5;
end

else if(a[4]==1)
begin
k=4;
end


else if(a[3]==1)
begin
k=3;
end

else if(a[2]==1)
begin
k=2;
end

else if(a[1]==1)
begin
k=1;
end

else 
begin
k=0;
end

if (b[63]==1)
begin
l=63;
end
else if(b[62]==1)
begin
l=62;
end

else if(b[61]==1)
begin
l=61;
end

else if(b[60]==1)
begin
l=60;
end

else if(b[59]==1)
begin
l=59;
end

else if(b[58]==1)
begin
l=58;
end
else if (b[57]==1)
begin
l=57;
end
else if(b[56]==1)
begin
l=56;
end

else if(b[55]==1)
begin
l=55;
end

else if(b[54]==1)
begin
l=54;
end

else if(b[53]==1)
begin
l=53;
end

else if(b[52]==1)
begin
l=52;
end

else if(b[51]==1)
begin
l=51;
end

else if(b[50]==1)
begin
l=50;
end

else if(b[49]==1)
begin
l=49;
end
else if(b[48]==1)
begin
l=48;
end
else if(b[47]==1)
begin
l=47;
end
else if(b[46]==1)
begin
l=46;
end
else if(b[45]==1)
begin
l=45;
end

else if(b[44]==1)
begin
l=44;
end

else if(b[43]==1)
begin
l=43;
end

else if(b[42]==1)
begin
l=42;
end

else if(b[41]==1)
begin
l=41;
end

else if(b[40]==1)
begin
l=40;
end

else if(b[39]==1)
begin
l=39;
end

else if(b[38]==1)
begin
l=38;
end

else if(b[37]==1)
begin
l=37;
end

else if(b[36]==1)
begin
l=36;
end


else if(b[35]==1)
begin
l=35;
end

else if(b[34]==1)
begin
l=34;
end

else if(b[33]==1)
begin
l=33;
end
else if (b[32]==1)
begin
l=32;
end

else if(b[31]==1)
begin
l=31;
end

else if(b[30]==1)
begin
l=30;
end

else if(b[29]==1)
begin
l=29;
end

else if(b[28]==1)
begin
l=28;
end

else if(b[27]==1)
begin
l=27;
end

else if(b[26]==1)
begin
l=26;
end
else if (b[25]==1)
begin
l=25;
end
else if(b[24]==1)
begin
l=24;
end

else if(b[23]==1)
begin
l=23;
end

else if(b[22]==1)
begin
l=22;
end

else if(b[21]==1)
begin
l=21;
end

else if(b[20]==1)
begin
l=20;
end

else if(b[19]==1)
begin
l=19;
end

else if(b[18]==1)
begin
l=18;
end

else if(b[17]==1)
begin
l=17;
end
else if(b[16]==1)
begin
l=16;
end
else if(b[15]==1)
begin
l=15;
end
else if(b[14]==1)
begin
l=14;
end
else if(b[13]==1)
begin
l=13;
end

else if(b[12]==1)
begin
l=12;
end

else if(b[11]==1)
begin
l=11;
end

else if(b[10]==1)
begin
l=10;
end

else if(b[9]==1)
begin
l=9;
end

else if(b[8]==1)
begin
l=8;
end

else if(b[7]==1)
begin
l=7;
end

else if(b[6]==1)
begin
l=6;
end

else if(b[5]==1)
begin
l=5;
end

else if(b[4]==1)
begin
l=4;
end


else if(b[3]==1)
begin
l=3;
end

else if(b[2]==1)
begin
l=2;
end

else if(b[1]==1)
begin
l=1;
end

else 
begin
l=0;
end

m=0;
n=0;
sum1 = k-num;
sum2 = l-num;
if (sum1<0)
begin
sum1 = -1;
end

if (sum2 <0)
begin
sum2 = -1;
end

sum = sum1+sum2+2;  // number of zeros which will be appended at the end of multiplication


if (num==10)
begin
for (i=0;i<10;i=i+1)
begin
	m[10-1-i]=a[k-i];
	n[10-1-i]=b[l-i];
end
end

if (num==9)
begin
for (i=0;i<9;i=i+1)
begin
	m[9-1-i]=a[k-i];
	n[9-1-i]=b[l-i];
end
end

if (num==8)
begin
for (i=0;i<8;i=i+1)
begin
	m[8-1-i]=a[k-i];
	n[8-1-i]=b[l-i];
end
end

else
begin
for (i=0;i<7;i=i+1)
begin
	m[7-1-i]=a[k-i];
	n[7-1-i]=b[l-i];
end
end

if (k<=num)
begin
m = a;
end

if (l<=num)
begin
n = b;
end

y=0;
y=m*n;
y=y<<sum;   // appending of zeros at the end of multiplication
end
endmodule

/* module tb_approx_multiplier_1();
wire [127:0]y;
reg [63:0]a;
reg [63:0]b;
parameter num=7;
approx_multiplier_1 #(num) M1(a,b,y);
initial begin
#0 a=56783567; b=672323;
#5 a=4012869; b=35343233;
#5 a=5345664; b=655677;
#5 a=1213313; b=987652;
#5 a=94384884; b=3344333;
end

initial begin
$display ("time  a   	b   	y  ");
$monitor (" %0d     %0d     %0d     %0d ",$time,a,b,y);
end
endmodule */
 


