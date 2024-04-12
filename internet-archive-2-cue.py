import sys, json, re


if __name__ == '__main__':
    in_file = sys.argv[1]

    with open(in_file) as f:
        ori = f.read()
        cnt = json.loads(ori)
        trks = []
        i = 0
        for item in cnt:
            ss = re.match(r'disc\d+/(.*)\.flac', item['file'])
            out_file = ss.group(1) + '.cue'
            of = open(out_file, 'w')
            of.write('TITLE "' + item['tracks'][0]['file_md']['album'] + '"\n')
            of.write('PERFORMER "' + item['tracks'][0]['file_md']['artist'] + '"\n')
            of.write('FILE "' + ss.group(1) +'.flac" WAVE' + '\n')
            n = 0
            for track in item['tracks']:
                trks.append({})
                trks[n]['title'] = track['file_md']['title']
                ms = track['segments']['final']['duration']
                sec = int((ms/1000)%60)
                min = int((ms/(1000*60))%60)
                hr = int((ms/(1000*60*60))%60)
                trks[n]['index'] = str(hr) +':' + str(min) + ':' + str(sec)
                n = n + 1
                of.write('  TRACK ' + str(n) + ' AUDIO\n')
                of.write('    TITLE "' + track['file_md']['title'] + '"\n')
                of.write('    INDEX 01 ' + str(hr) +':' + str(min) + ':' + str(sec) + '\n')
            #print(trks)
            trks.clear()
            i = i + 1
        of.close()
        f.close()