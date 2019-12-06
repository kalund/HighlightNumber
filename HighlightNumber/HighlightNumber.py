import sublime
import sublime_plugin

class HighlightnumberListener(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        highlighted = view.substr(view.sel()[0])
        if isinstance(highlighted, str):
            self._showPopup(view, highlighted)
            # Testnumber = 456 100 165465163514694964964986 1110000011100111001001

    def _showPopup(self, view, highlighted):
        lenDec = 0
        lenHex = 0
        lenBin = 0
        valAsHex = None
        valAsBin= None
        valAsDec= None
        # The order of these trys aren't random!!!

        try:
            valAsHex = int(highlighted, 16)
            isHex = True
            lenHex = len(str(valAsHex))
            if lenHex == 0:
                lenHex = len('{:x}'.format(valAsHex))
            if lenBin == 0:
                lenBin = len('{:b}'.format(valAsHex))
            if lenDec == 0:
                lenDec = len('{:d}'.format(valAsHex))
        except:
            isHex = False

        try:
            valAsDec = int(highlighted)
            isDec = True
            if lenHex == 0:
                lenHex = len('{:x}'.format(valAsDec))
            if lenBin == 0:
                lenBin = len('{:b}'.format(valAsDec))
            if lenDec == 0:
                lenDec = len('{:d}'.format(valAsDec))
        except:
            isDec = False

        try:
            valAsBin = int(highlighted, 2)
            isBin = True
            if lenHex == 0:
                lenHex = len('{:x}'.format(valAsBin))
            if lenBin == 0:
                lenBin = len('{:b}'.format(valAsBin))
            if lenDec == 0:
                lenDec = len('{:d}'.format(valAsBin))
        except:
            isBin = False

        contents  = '<u>{}'.format(highlighted) + '&nbsp;'*4
        contents += 'DEC ' + '&nbsp;'*lenDec
        contents += 'HEX ' + '&nbsp;'*(lenHex)
        contents += 'BIN ' + '&nbsp;'*(lenBin-7)
        contents += '&nbsp;'*5
        contents += '</u><br>'

        if isDec:
            # contents += '{}&nbsp;&nbsp;&nbsp;&nbsp;'.format(highlighted.strip())
            contents += 'DEC ' +'&nbsp;'*(len(highlighted.strip()))
            contents += '{} '.format(valAsDec) + '&nbsp;'*(3+lenDec-len('{}'.format(valAsDec)))
            contents += '0x{:X} '.format(valAsDec) + '&nbsp;'*(3+lenHex-len('0x{:x}'.format(valAsDec)))
            contents += '0b{:b} '.format(valAsDec)
            contents += '<br>'
            # contents += '{} = 0b{:032b}, = 0x{:08x}<br>'.format(highlighted, valAsDec, valAsDec)
        if isHex:
            # contents += '0x{}&nbsp;&nbsp;'.format(highlighted.strip())
            contents += 'HEX ' +'&nbsp;'*(len(highlighted.strip()))
            contents += '{} '.format(valAsHex) + '&nbsp;'*(3+lenDec-len('{}'.format(valAsHex)))
            contents += '0x{:X} '.format(valAsHex) + '&nbsp;'*(3+lenHex-len('0x{:x}'.format(valAsHex)))
            contents += '0b{:b} '.format(valAsHex)
            contents += '<br>'
            # contents += '0x{} = 0b{:032b}, = {}<br>'.format(highlighted, valAsHex, valAsHex)
        if isBin:
            # contents += '0b{}&nbsp;&nbsp;'.format(highlighted.strip())
            contents += 'BIN ' +'&nbsp;'*(len(highlighted.strip()))
            contents += '{} '.format(valAsBin) + '&nbsp;'*(3+lenDec-len('{}'.format(valAsBin)))
            contents += '0x{:X} '.format(valAsBin) + '&nbsp;'*(3+lenHex-len('0x{:x}'.format(valAsBin)))
            contents += '0b{:b} '.format(valAsBin)
            contents += '<br>'
            # 1111001101101
        if isBin or isDec or isHex:
            view.show_popup(contents, max_width = 800, max_height = 400)
        # view.set_status("mytag", highlighted+'\n')
