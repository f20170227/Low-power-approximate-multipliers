`timescale 1ns/1ps

///////////// 32*32 bit multiplier scheme 2/////////

module approx_multiplier_1 (input [31:0]a, input [31:0]b, output reg [63:0]y );
integer i,j,sum1,sum2,sum,k,l,num;  //k and l are the bits which will detect leading 1
reg [7:0]m=0;   // m and n are the two numbers to be multiplied
reg [7:0]n=0;

always @(a or b)
begin

if (a[31] || a[30] || a[29] || a[28] || b[31] || b[30] || b[29] || b[28] )
begin
num=8;
end

else if ( a[27] || a[26] || a[25] || a[24] || b[27] || b[26] || b[25] || b[24] )
begin
num=7;
end

else
begin
num=6;
end

// while statement is not synthesisable in verilog so we nested if else statement is used

if (a[31]==1)
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


if (b[31]==1)
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

else if (b[15]==1)
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

sum = sum1+sum2+2;  // number of zeros which will be appended at the endof multiplication



if (num==8)
begin
for (i=0;i<8;i=i+1)
begin
	m[8-1-i]=a[k-i];
	n[8-1-i]=b[l-i];
end
end

else if (num==7)
begin
for (i=0;i<7;i=i+1)
begin
	m[7-1-i]=a[k-i];
	n[7-1-i]=b[l-i];
end
end

else
begin
for (i=0;i<6;i=i+1)
begin
	m[6-1-i]=a[k-i];
	n[6-1-i]=b[l-i];
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


