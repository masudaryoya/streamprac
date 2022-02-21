import streamlit as st
import numpy as np

import time

def main():
    st.title('hello!')
    st.subheader("aaa")
    array = np.arange(1,6)

    selected_item = st.radio('Which do you like?',array)
    selected_item = st.slider('select',1,10,5)

    if selected_item%2 == 0:
        st.write('偶数')
    else:
        st.write('奇数')

    st.latex(r'''
         a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
         \sum_{k=0}^{n-1} ar^k =

         a \left(\frac{1-r^{n}}{1-r}\right)
         ''')
    st.latex(r'y={0}x^{0}+1'.format(selected_item,selected_item))
    x = np.linspace(0,2,100)
    y = np.power(-1,selected_item) *x**selected_item+1
    # """
    # # 章
    # ## 節
    # ### 項
    #
    # ``` python
    # import streamlit as st
    # import numpy as np
    # ```
    # """
    #
    # df = pd.DataFrame(
    #     np.random.rand(20,3),
    #     columns=['a','b','c']
    # )
    # st.area_chart(df)
    #
    #
    # fig = plt.figure(figsize=(20,6))
    # ax = fig.add_subplot()
    # # x = np.random.normal(loc=.0, scale=1., size=(100,))
    # ax.plot(x,y)
    # # プレースホルダにグラフを書き込む
    #
    # # データを追加する
    # # additional_data = np.random.normal(loc=.0, scale=1., size=(10,))
    # # x = np.concatenate([x, additional_data])
    # # # グラフを描画し直す
    # # ax.plot(x)
    # # プレースホルダに書き出す
    # st.pyplot(fig)
    #
    # selected_item = st.selectbox('Which do you like?',
    #                              ['Dog', 'Cat'])
    # st.write(f'Selected: {selected_item}')

    st.write('プログレスバー')
    'Start'
    latest = st.empty()
    bar = st.progress(0)

    for i in range(100):
        latest.text(f'Iteration {i+1}')
        bar.progress(i+1)
        time.sleep(0.1)


    letfcol,rightcol = st.columns(2)
    button = letfcol.button('右に表示')
    if button:
        rightcol.write('表示')

    expander = st.expander('問い合わせ')
    expander.write('内容')



if __name__ == '__main__':
    main()