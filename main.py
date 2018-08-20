import os
import sys
import glob
import argparse
import cv2

parser = argparse.ArgumentParser(
  prog='frame2video',
  description='convert frames into video',
  add_help=True
)

parser.add_argument('-d', '--directory', required=True, help='directory with frames labeled by consequent numbers')
parser.add_argument('-o', '--output', required=False, help='output filename', default='output.avi')

args = parser.parse_args()
print('===== frame2video =====')
print('directory path: {}'.format(os.path.abspath(args.directory)))
print('output file   : {}'.format(os.path.abspath(args.output)))
print('=======================')
img_list = sorted(glob.glob(os.path.join(args.directory, '*.jpg')))

img = cv2.imread(img_list[0])
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
writer = cv2.VideoWriter(args.output, fourcc, 30.0, (img.shape[1], img.shape[0]))

for idx, img_path in enumerate(img_list):
  img = cv2.imread(img_path)
  writer.write(img)
  sys.stdout.write('\r' + 'process: {:3d}%'.format((int)((idx + 1) / len(img_list) * 100)))
  sys.stdout.flush()

sys.stdout.write('\nDone!\n')
writer.release()