import sys, json, re

def convert2hms(ms):
    sec = int((ms/1000)%60)
    min = int((ms/(1000*60))%60)
    hr = int((ms/(1000*60*60))%60)
    hms = str(hr) +':' + str(min) + ':' + str(sec)

if __name__ == '__main__':
    in_file = sys.argv[1]
    with open(in_file) as f:
        ori = f.read()
        cnt = json.loads(ori)
        for item in cnt:
            ss = re.match(r'disc\d+/(.*)\.flac', item['file'])
            out_file = ss.group(1) + '.cue'
            of = open(out_file, 'w')
            of.write('TITLE "' + item['tracks'][0]['file_md']['album'] + '"\n')
            of.write('PERFORMER "' + item['tracks'][0]['file_md']['artist'] + '"\n')
            of.write('FILE "' + ss.group(1) +'.flac" WAVE' + '\n')
            for track in item['tracks']:
                title = track['file_md']['title']
                #index0 = convert2hms(track['segments']['initial']['start'])
                index1 = convert2hms(track['segments']['final']['duration'])
                of.write('  TRACK ' + str(n) + ' AUDIO\n')
                of.write('    TITLE "' + title + '"\n')
                #of.write('    INDEX 00 ' + index0 + '\n')
                of.write('    INDEX 01 ' + index1 + '\n')
            of.close()