%��������� �������� � ��������� �� 0,001.
%������������ ������ 1
% ������ 20 ������� 22
%�����: ����� �.�.
%����� ����� ���� 453504 2015

syms T Integral x
T = taylor( exp(-3*x^2/4) );
Integral = int( T,0,0.4 );
disp( Integral );

