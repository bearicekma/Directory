{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1xMphHk5BfeKCMg3gUsEGjVpKO4DZmxsr",
      "authorship_tag": "ABX9TyOJM7DlNx7/dIPZ+ABTJCh6",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/bearicekma/Directory/blob/main/streamlit_app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# モジュールの読み込み\n",
        "import pandas as pd\n",
        "import streamlit as st\n",
        "import pygwalker as pyg\n",
        "\n",
        "# 初期設定\n",
        "st.set_page_config(layout=\"wide\")\n",
        "\n",
        "# CSVファイル取得（サイドパネル）\n",
        "df = None\n",
        "with st.sidebar:\n",
        "    input = st.file_uploader(\"Choose a CSV file\")\n",
        "    if input is not None:\n",
        "        df = pd.read_csv(input)\n",
        "\n",
        "# Graphic Walker 操作（メインパネル）\n",
        "if df is not None:\n",
        "    output = pyg.walk(df, env='Streamlit')\n",
        "    st.write(output)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uolL8zF4bIW-",
        "outputId": "40155a07-5615-4d46-977f-8fff0439c6ef"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing streamlit_app.py\n"
          ]
        }
      ]
    }
  ]
}