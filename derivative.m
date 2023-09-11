clc
% 加载神经网络模型
load('net.mat');
gpa=4.43;
toefl=100;
sat=1100;
ap=20;
% 替换以下示例数据为您的输入数据
input_data = [gpa; toefl; sat; ap];
% 进行推理
output1 = sim(net, input_data); 
% 四舍五入输出结果
rounded_output1 = round(output1);
% 显示结果
disp("your result:"+rounded_output1);

% 替换以下示例数据为您的输入数据
input_data = [gpa+0.05; toefl; sat; ap];
% 进行推理
output2 = sim(net, input_data); 
% 四舍五入输出结果
rounded_output2 = round(output2);
% 显示结果
disp(rounded_output2);
derivative12=rounded_output1-rounded_output2;
disp("ranking over gpa:"+derivative12);

% 替换以下示例数据为您的输入数据
input_data = [gpa; toefl+5; sat; ap];
% 进行推理
output3 = sim(net, input_data); 
% 四舍五入输出结果
rounded_output3 = round(output3);
% 显示结果
disp(rounded_output3);
derivative13=rounded_output1-rounded_output3;
disp("ranking over toefl:"+derivative13);

% 替换以下示例数据为您的输入数据
input_data = [gpa; toefl; sat+10; ap];
% 进行推理
output4 = sim(net, input_data); 
% 四舍五入输出结果
rounded_output4 = round(output4);
% 显示结果
disp(rounded_output4);
derivative14=rounded_output1-rounded_output4;
disp("ranking over sat:"+derivative14);

% 替换以下示例数据为您的输入数据
input_data = [gpa; toefl; sat; ap+1];
% 进行推理
output5 = sim(net, input_data); 
% 四舍五入输出结果
rounded_output5 = round(output5);
% 显示结果
disp(rounded_output5);
derivative15=rounded_output1-rounded_output5;
disp("ranking over ap:"+derivative15);

list = [derivative12,derivative13,derivative14,derivative15,gpa,toefl,sat,ap,rounded_output1];
disp(list);
writematrix(list,'demo.xlsx');