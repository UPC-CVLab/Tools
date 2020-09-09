import csv

class Logger(object):

    def __init__(self, path, header, mode='w'):
        self.log_file = open(path, mode=mode)
        self.logger = csv.writer(self.log_file, delimiter='\t')

        if mode != 'a':
            self.logger.writerow(header)

        self.header = header

    def __del(self):
        self.log_file.close()

    def log(self, values):
        write_values = []
        for col in self.header:
            assert col in values
            write_values.append(values[col])

        self.logger.writerow(write_values)
        self.log_file.flush()

train_logger = Logger(os.path.join(args.result_path, 'train.log'),
                          ['epoch', 'loss', 'acc1', 'acc5', 'lr'], mode=mode)

train_logger.log({
            'epoch': epoch+1,
            'loss': '{:.4f}'.format(train_loss),
            'acc1': '{:.2f}'.format(train_acc1.item()),
            'acc5': '{:.2f}'.format(train_acc5.item()),
            'lr': '{:.6f}'.format(optimizer.param_groups[0]['lr'])
        })