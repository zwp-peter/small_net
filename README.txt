author=zwp my email:1834586762@qq.com
亲爱的同志，很高兴能在这里与你相见，我相信你从来没有见过如此生动活泼的
说明文件，别着急让我们慢慢来哦~
1.首先你得把你的pytorch环境弄好，这里推荐您使用anaconda
2.安装好所有的依赖包，注意啦，当你使用了VPN时，您将会在pycharm中无法安装软件包
3.准备好你的数据集好朋友，没有数据集跑个der
4.train.py 142行确保数据集路径正确
5.train.py的13-19行选择你要使用的模型，另外70-87行也需要修改，具体怎么改，傻子都知道
6.class_indices.json是吧懂的都懂
7.train.py149行，如果有显卡那就不用改了，用显卡跑就行，没有显卡就改成：
  parser.add_argument('--device', default='cuda:cpu', help='device id (i.e. 0 or 0,1 or cpu)')
8.如果你out of memory了，那说明你的GPU内存不够，可以更改一下batch size参数，让他更小
什么是batchsize？参考这篇文章：https://blog.csdn.net/qq_34886403/article/details/82558399
9.tensorboard --logdir==.

10.predict.py导入需要预测的模型，然后39行需要修改，44行修改模型文件

有2000个数据，分成4个batch，那么batch size就是500。运行所有的数据进行训练，完成1个epoch，需要进行4次iterations。