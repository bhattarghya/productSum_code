import prod_sum


def test_ProductSum():
    assert prod_sum.ProductSum([2,4,[3,-4,[2,3],[5]],[6,[9]],8])== 161
    assert prod_sum.ProductSum([[6,[[[6,8]]]]])== 348
    assert prod_sum.ProductSum([1,1,[1,1,[1]]]) == 10
    assert prod_sum.ProductSum([[[1]]])==4
    assert prod_sum.ProductSum([])is None
    
