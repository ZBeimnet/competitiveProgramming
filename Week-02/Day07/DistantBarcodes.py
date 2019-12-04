def rearrange_barcodes(barcodes):
    barcode_length = len(barcodes)
    code_count = [0] * 10000
    arranged_barcode = []

    # counting the repetition of each letter
    for i in range(barcode_length):
        code_count[barcodes[i]] += 1

    previous_code = 0
    counter = barcode_length
    while counter > 0:
        max_index = 0
        for i in range(barcode_length):
            if code_count[i] > code_count[max_index] \
                    and barcodes[i] != previous_code:
                max_index = i

        arranged_barcode.append(barcodes[max_index])
        previous_code = barcodes[max_index]
        code_count[max_index] -= 1
        counter -= 1

    return arranged_barcode


print(rearrange_barcodes([1,1,1,2,2,2]))
