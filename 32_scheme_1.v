`timescale 1ns/1ps



/////////// 32*32 bit multiplier scheme 1///////////

module approx_32 (input [31:0]a, input [31:0]b, output reg [63:0]y);
integer i,j,k,l,sum1,sum2,sum;
parameter num=6;
reg [5:0]m=0;   // m and n are the two partial numbers 
reg [5:0]n=0;

always @(a or b)
begin


if(a[31]==1)
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


if(b[31]==1)
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

sum = sum1+sum2+2;

for (i=0;(i<num);i=i+1)
begin
	m[num-1-i]=a[k-i];
end

for (j=0;(j<num);j=j+1)
begin
	n[num-1-j]=b[l-j];
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
y=y<<sum;




end
endmodule


/* module tb_approx_32();
wire [63:0]y;
reg [31:0]a;
reg [31:0]b;
parameter num=6;
approx_32 #(num) M1(a,b,y);
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



