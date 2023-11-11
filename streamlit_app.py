{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1xMphHk5BfeKCMg3gUsEGjVpKO4DZmxsr",
      "authorship_tag": "ABX9TyMdirlN0OptQaDE2k5KkdfJ"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "# モジュールの読み込み\n",
        "import pandas as pd\n",
        "import streamlit as st\n",
        "import pygwalker as pyg\n",
        "\n",
        "st.title('Streamlitへようこそ')\n",
        "\n",
        "# # 初期設定\n",
        "# st.set_page_config(layout=\"wide\")\n",
        "\n",
        "# # CSVファイル取得（サイドパネル）\n",
        "# df = None\n",
        "# with st.sidebar:\n",
        "#     input = st.file_uploader(\"Choose a CSV file\")\n",
        "#     if input is not None:\n",
        "#         df = pd.read_csv(input)\n",
        "\n",
        "# # Graphic Walker 操作（メインパネル）\n",
        "# if df is not None:\n",
        "#     output = pyg.walk(df, env='Streamlit')\n",
        "#     st.write(output)"
      ],
      "metadata": {
        "id": "uolL8zF4bIW-"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}