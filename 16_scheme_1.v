`timescale 1ns/1ps

/////////// 16*16 bit multiplier scheme 1///////////

module approx_multiplier_1 (input [15:0]a, input [15:0]b, output reg [31:0]y);
integer i,j,k,l,sum1,sum2,sum,c;
parameter num=6;
reg [num-1:0]m=0;   // m and n are the two partial numbers
reg [num-1:0]n=0;

always @(a or b)
begin
if (a[15]==1)
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

if (b[15]==1)
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

else if(a[6]==1)
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

/* module tb_approx_multiplier_1_5();
wire [31:0]y;
reg [15:0]a;
reg [15:0]b;
parameter num=6;
approx_multiplier_1 #(num) M1(a,b,y);
initial begin
#0 a=56783; b=6723;
#5 a=16'hFFAA; b=16'h08FA;
#5 a=16'h0892; b=16'h081A;
#5 a=16'h0A12; b=16'h01FB;
#5 a=16'h0392; b=16'hC8CA;
end

initial begin
$display ("time  a   	b   	y ");
$monitor (" %0d     %0d     %0d     %0d ",$time,a,b,y);
end
endmodule

 */
