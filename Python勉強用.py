{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "102bCTKQwupVx4KbgFncAimVBXzrGmsOM",
      "authorship_tag": "ABX9TyMSn6iWaNTM9eMuXkVPCKAH",
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
        "<a href=\"https://colab.research.google.com/github/bearicekma/Directory/blob/main/Python%E5%8B%89%E5%BC%B7%E7%94%A8.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 繰り返し構文(for, while)について"
      ],
      "metadata": {
        "id": "14IZg-rInynA"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "kvU2baB1Joux",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "85980b40-3388-4056-fa37-bcad5529adf6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n"
          ]
        }
      ],
      "source": [
        "i = 0\n",
        "while i < 5:\n",
        "    print(i)\n",
        "    i += 1"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(5):\n",
        "    print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HfFPLvplJBgk",
        "outputId": "cf8dbf41-6046-4881-fc84-ec302c85ce6d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 偶数列　range(始点、終点、step)\n",
        "for i in range(2,11,2):\n",
        "    print(i)\n",
        "\n",
        "print(\"===\")\n",
        "\n",
        "for i in range(1, 11):\n",
        "    if i % 2 == 0:\n",
        "        print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "62UuIDMZKWyj",
        "outputId": "eebcd50d-eff5-4849-ae5f-adfecb4c1a79"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2\n",
            "4\n",
            "6\n",
            "8\n",
            "10\n",
            "===\n",
            "2\n",
            "4\n",
            "6\n",
            "8\n",
            "10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 奇数の要素のみ\n",
        "list = [1,2,3,4,5,6,7,8,9,10]\n",
        "for item in list:\n",
        "    if item % 2 != 0:\n",
        "        print(item)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rKc9LZAlLTJN",
        "outputId": "2ec2b565-a3fe-47b0-d197-588df33e9b59"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "3\n",
            "5\n",
            "7\n",
            "9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# リストの要素を全て出力\n",
        "list = [\"ピチュー\", \"ピカチュウ\", \"ライチュウ\", \"ピィ\", \"ピッピ\", \"ピクシー\"]\n",
        "\n",
        "for item in list:\n",
        "    print(item)\n",
        "\n",
        "for item in range(len(list)): # range(len(list)) <= リストの要素数だけ抽出できる\n",
        "    print(list[item]) # スライサーで表示"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "29QhrBQLO5U7",
        "outputId": "4738d27f-9f61-41df-cae6-9524a15a8e7a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ピチュー\n",
            "ピカチュウ\n",
            "ライチュウ\n",
            "ピィ\n",
            "ピッピ\n",
            "ピクシー\n",
            "ピチュー\n",
            "ピカチュウ\n",
            "ライチュウ\n",
            "ピィ\n",
            "ピッピ\n",
            "ピクシー\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 空リストの各要素に代入\n",
        "list = []\n",
        "\n",
        "# 代入\n",
        "for i in range(5):\n",
        "    list.append(\"ピカチュウ\")\n",
        "\n",
        "# 表示\n",
        "for item in list:\n",
        "    print(item)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GgM5FeMwSHZ2",
        "outputId": "2b288fdd-6f15-44fb-d16f-f60af954a2ad"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ピカチュウ\n",
            "ピカチュウ\n",
            "ピカチュウ\n",
            "ピカチュウ\n",
            "ピカチュウ\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "del list"
      ],
      "metadata": {
        "id": "7j2QDErgGwwm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 高階関数"
      ],
      "metadata": {
        "id": "AB6O2Clfvl0v"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## map関数\n",
        "\n",
        "> https://qiita.com/kubochiro/items/b32a3f723addae752a38#:~:text=map()%E9%96%A2%E6%95%B0%E3%81%AF%E3%80%81Python,%E3%81%9F%E3%82%81%E3%81%AB%E4%BD%BF%E7%94%A8%E3%81%95%E3%82%8C%E3%81%BE%E3%81%99%E3%80%82\n",
        "\n"
      ],
      "metadata": {
        "id": "EL21oUgmEtk_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# listの各要素に対して +2加算する処理\n",
        "num_list = [1,2,3,4,5]\n",
        "\n",
        "# map関数で　第1引数に関数（lambda関数）、第2引数に対象要素のリスト。list関数でlist化する。\n",
        "num_list = list(map(lambda x: x + 2, num_list))\n",
        "\n",
        "print(num_list)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AcxKN3LjELSh",
        "outputId": "c05ad6c9-34ef-4b61-ec5b-ea15a2431b2a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[3, 4, 5, 6, 7]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num_list = [3,4,1,5,2]\n",
        "\n",
        "num_list = list(map(lambda x: x*3+2, num_list))\n",
        "\n",
        "print(num_list)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f8u8Hh2KHNk-",
        "outputId": "714e2ace-83fb-4796-a4f4-5552030ddde6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[11, 14, 5, 17, 8]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "poke_list = [\"ピィ\",\"ピッピ\",\"ピクシー\"]\n",
        "\n",
        "poke_list = list(map(lambda x: \"〇\" + x + \"〇\", poke_list))\n",
        "\n",
        "for poke in poke_list:\n",
        "    print(poke)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bekyRsotMJs_",
        "outputId": "a5453c1e-4e9c-481b-c671-07b40aa35745"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "〇ピィ〇\n",
            "〇ピッピ〇\n",
            "〇ピクシー〇\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## filter関数"
      ],
      "metadata": {
        "id": "EyToNk3d0UOY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# ラムダ式の条件（Trueを返した条件）によって、リスト内の要素を抽出\n",
        "\n",
        "num_list = [1,2,3,4,5,6,7,8]\n",
        "# リストから偶数のみを抽出\n",
        "num_list2 = list(filter(lambda num: num % 2 == 0, num_list))\n",
        "print(num_list2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V_SZ5kjGMyeL",
        "outputId": "4039c790-513b-44db-834f-051274d3d83b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[2, 4, 6, 8]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# リストから3以上の要素のみ抽出\n",
        "num_list = [4,6,2,3,5,1]\n",
        "\n",
        "num_list = list(filter(lambda num: num >= 3, num_list))\n",
        "\n",
        "for num in num_list:\n",
        "    print(num)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xO1ZMsYo0zx0",
        "outputId": "9afefcfb-08d7-492e-9ec4-be9a17faef5f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4\n",
            "6\n",
            "3\n",
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "poke_list = [\"ピチュー\", \"ピカチュウ\", \"ライチュウ\", \"ピィ\", \"ピッピ\", \"ピクシー\",\"ピカチュウ\"]\n",
        "\n",
        "poke_list = list(filter(lambda poke: poke == \"ピカチュウ\", poke_list))\n",
        "\n",
        "for poke in poke_list:\n",
        "    print(poke)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tL6p1g433MsJ",
        "outputId": "8c664409-61ca-48e1-adaf-7d45fa9e2045"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ピカチュウ\n",
            "ピカチュウ\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## any関数、all関数"
      ],
      "metadata": {
        "id": "0DYcwz5K4Iid"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 条件式に当てはまる場合はTrueを、そうでない場合はFalseを返すany関数。any(条件式　繰り返しfor文)\n",
        "num_list = [1,2,3,4,5]\n",
        "\n",
        "exist = any([num >= 6 for num in num_list]) # リスト内包表記になってる\n",
        "\n",
        "if exist:\n",
        "    print(exist)\n",
        "    print(\"5以上の要素が存在します\")\n",
        "else:\n",
        "    print(exist)\n",
        "    print(\"5以上の要素は存在しません\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q13zZ82M3u9y",
        "outputId": "d58fcb96-acd3-4f3c-ce50-333319f5b854"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n",
            "5以上の要素は存在しません\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# all関数　リスト内の全ての要素が条件を満たしている=True、そうでない場合=Falseを返す\n",
        "num_list = [4,5,6,7,8]\n",
        "\n",
        "exist = all([num >= 5 for num in num_list]) # リスト内包表記になってる\n",
        "\n",
        "if exist:\n",
        "    print(exist)\n",
        "    print(\"全ての要素は5以上です\")\n",
        "else:\n",
        "    print(exist)\n",
        "    print(\"5以上でない要素が含まれています\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9fc6L0p24kZB",
        "outputId": "1e787832-d53a-448f-83c9-633ff98ca5b7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n",
            "5以上でない要素が含まれています\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## max, min, sum関数"
      ],
      "metadata": {
        "id": "XqKubXvrYEbJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# max関数。リスト内の最大値を返す\n",
        "num_list = [3,4,5,2,1]\n",
        "\n",
        "num = max(num_list)\n",
        "print(num)\n",
        "\n",
        "# min関数。リスト内の最小値を返す\n",
        "num = min(num_list)\n",
        "print(num)\n",
        "\n",
        "# sum関数。リスト内の合計値を返す\n",
        "num = sum(num_list)\n",
        "print(num)"
      ],
      "metadata": {
        "id": "C54gKe4y5vSV",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6d78603c-81c5-4513-e220-963fe6c100de"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n",
            "1\n",
            "15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 文字列の長さが一番多いものを求めたいとき\n",
        "poke_list = [\"ピチュー\", \"ピカチュウ\", \"ライチュウ\", \"ピィ\", \"ピッピ\", \"ピクシー\"]\n",
        "\n",
        "# max関数の第2引数にkey=lenを指定\n",
        "len_max = max(poke_list, key=len)\n",
        "print(len_max)\n",
        "type(len_max)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zHXOduu7fTGI",
        "outputId": "6e7d4d52-2ab3-4d43-d12a-7225e8cabf5b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ピカチュウ\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 要素の中の一番大きい文字列の長さを求めたいとき\n",
        "poke_list = [\"ピチュー\", \"ピカチュウ\", \"ライチュウ\", \"ピィ\", \"ピッピ\", \"ピクシー\"]\n",
        "\n",
        "len_max = max([len(poke) for poke in poke_list]) # これもlist内包表記\n",
        "print(len_max)\n",
        "type(len_max)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JUzpqOb1hS6N",
        "outputId": "2b13a2a7-9914-439d-fbe5-a80d5d9e1b13"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "int"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# set関数, sorted関数"
      ],
      "metadata": {
        "id": "yH1SXzJ5noFE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# set関数=> リストの要素の中から重複を削除する\n",
        "num_list = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]\n",
        "uniqlist = []\n",
        "\n",
        "uniqlist1 = set(num_list)\n",
        "print(uniqlist1)\n",
        "print(type(uniqlist1)) # set型（重複のないリストみたいな型）を返す\n",
        "\n",
        "uniqlist2 = list(set(num_list)) # list型に変換する\n",
        "print(uniqlist2)\n",
        "print(type(uniqlist2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a9so69fgjMiU",
        "outputId": "cad56442-bef6-45c1-c195-7de5b23bf634"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{1, 2, 3}\n",
            "<class 'set'>\n",
            "[1, 2, 3]\n",
            "<class 'list'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# sorted関数　=> 名前のとおりソートする関数\n",
        "num_list = [3,6,2,7,1,8,10,9,4,5]\n",
        "\n",
        "num_list = sorted(num_list)\n",
        "print(num_list)\n",
        "\n",
        "# 降順にする引数reverse\n",
        "num_list = sorted(num_list, reverse=True)\n",
        "num_list\n",
        "\n",
        "# 文字列の長さ順で並び替える。第2引数にkey=lenを指定。\n",
        "poke_list = [\"ピチュー\", \"ピカチュウ\", \"ライチュウ\", \"ピィ\", \"ピッピ\", \"ピクシー\"]\n",
        "\n",
        "poke_list = sorted(poke_list, key=len)\n",
        "\n",
        "for poke in poke_list:\n",
        "    print(poke)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JINoQrfMoH6b",
        "outputId": "28f73c8d-bf28-42a6-8b72-3954b3e96509"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
            "ピィ\n",
            "ピッピ\n",
            "ピチュー\n",
            "ピクシー\n",
            "ピカチュウ\n",
            "ライチュウ\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 無名関数:lambda式"
      ],
      "metadata": {
        "id": "aKUWvIExKIat"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num_10 = 10\n",
        "\n",
        "# ラムダ式を変数add5に代入\n",
        "add5 = lambda num: num + 5\n",
        "\n",
        "print(add5(num=num_10))"
      ],
      "metadata": {
        "id": "Oj-b2LpOqP6V",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "02db0104-0b9c-4b3f-f6d8-04edcdb1ecf0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num_10 = 10\n",
        "num_20 = 20\n",
        "\n",
        "# ラムダ式を変数addに代入\n",
        "add = lambda num1, num2: num1 + num2\n",
        "\n",
        "print(add(num1=num_10, num2=num_20))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lhg5723SL6BV",
        "outputId": "a7b84aa4-e51f-4a62-96f9-4b395d488073"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "30\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num_10 = 10\n",
        "num_20 = 20\n",
        "\n",
        "num_print = lambda x: print(\"15以下です\") if x < 15 else print(\"15以上です\")\n",
        "\n",
        "num_print(x=num_10)\n",
        "num_print(x=num_20)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RqPqsis3MBzm",
        "outputId": "cb09fa75-722a-4600-fc69-8f2646f729ee"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15以下です\n",
            "15以上です\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# ラムダ式はリストに格納することも可能\n",
        "\n",
        "calc_list = [lambda a, b: a+b, lambda a, b: a-b, lambda a, b: a*b, lambda a, b: a/b, lambda a, b: a%b]\n",
        "\n",
        "for calc in calc_list:\n",
        "    print(calc(a=5,b=2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eHjwvzDSPKgJ",
        "outputId": "09d404d2-8a03-4e86-8b73-41d1eba78204"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7\n",
            "3\n",
            "10\n",
            "2.5\n",
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 文字数を足し合わせる関数\n",
        "pokemon1 = \"ピッピ\"\n",
        "pokemon2 = \"ピカチュウ\"\n",
        "\n",
        "len_add = lambda poke1, poke2: len(poke1) + len(poke2)\n",
        "\n",
        "print(len_add(poke1=pokemon1, poke2=pokemon2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WETmkDNTYjmp",
        "outputId": "6f28a9a6-d6f1-4c39-f49d-94ba9439856a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "8\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pokemon1 = \"ピッピ\"\n",
        "pokemon2 = \"ピカチュウ\"\n",
        "\n",
        "# pokemon1の文字列が長い場合はTrueを、そうでないならFalseを返す\n",
        "len_exist = lambda poke1, poke2:len(poke1) > len(poke2)\n",
        "\n",
        "if(len_exist(poke1=pokemon1, poke2=pokemon2)):\n",
        "    print(\"pokemon1の方が長いです\")\n",
        "else:\n",
        "    print(\"pokemon2の方が長いです\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1cguFCHDaJto",
        "outputId": "fb78a060-cdbc-472f-9662-679ffc75edc8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "pokemon2の方が長いです\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 演習問題"
      ],
      "metadata": {
        "id": "lmcD4NMIi1qw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# リストから奇数のみ抽出し、合計した要素を求める\n",
        "num_list = [8,7,2,1,6,5,9,4,10,3]\n",
        "\n",
        "result = sum(filter(lambda num: num % 2 != 0, num_list))\n",
        "print(result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CDtyyVlIdIZC",
        "outputId": "95955ff4-33da-4c2f-91cd-508f1f6ee3f0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "25\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 文字列が4で一番最後の要素のみ出力\n",
        "poke_list = [\"ピチュー\", \"ピカチュウ\", \"ライチュウ\", \"ピィ\", \"ピッピ\", \"ピクシー\",\"ププリン\", \"プリン\", \"プクリン\"]\n",
        "\n",
        "result = sorted(filter(lambda poke: len(poke) == 4, poke_list))\n",
        "result[-1]\n",
        "\n",
        "# 3番目までスライス\n",
        "result[0:3]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "soDx0KVdi_t6",
        "outputId": "941c84d5-ff95-454d-d1cf-4fe5572e5e87"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['ピクシー', 'ピチュー', 'プクリン']"
            ]
          },
          "metadata": {},
          "execution_count": 39
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# \"さん\"を付加して、文字列の長さで並び替え\n",
        "poke_list = [\"ピチュー\", \"ピカチュウ\", \"ライチュウ\", \"ピィ\", \"ピッピ\", \"ピクシー\",\"ププリン\", \"プリン\", \"プクリン\"]\n",
        "\n",
        "result = sorted(map(lambda poke: poke + \"さん\", poke_list), key=len)\n",
        "result"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CEojjCjOsrIC",
        "outputId": "b35aef36-0659-452e-ff92-9bf21763e635"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['ピィさん',\n",
              " 'ピッピさん',\n",
              " 'プリンさん',\n",
              " 'ピチューさん',\n",
              " 'ピクシーさん',\n",
              " 'ププリンさん',\n",
              " 'プクリンさん',\n",
              " 'ピカチュウさん',\n",
              " 'ライチュウさん']"
            ]
          },
          "metadata": {},
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# \"ピ\"を含む要素のみ抽出\n",
        "poke_list = [\"ピチュー\", \"ピカチュウ\", \"ライチュウ\", \"ピィ\", \"ピッピ\", \"ピクシー\",\"ププリン\", \"プリン\", \"プクリン\"]\n",
        "\n",
        "result = filter(lambda name: \"ピ\" in name, poke_list)\n",
        "list(result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2AQDRQz6xBzd",
        "outputId": "18ff4842-98f2-43e8-8e75-346cbb7db71b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['ピチュー', 'ピカチュウ', 'ピィ', 'ピッピ', 'ピクシー']"
            ]
          },
          "metadata": {},
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Pathlib"
      ],
      "metadata": {
        "id": "JhZDL0WuAqSa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pathlib"
      ],
      "metadata": {
        "id": "5LHUCy_T7szX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# カレントディレクトリを表示\n",
        "path = pathlib.Path.cwd() # 変数pathに代入できる\n",
        "print(path)\n",
        "type(path) # オブジェクトになる"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Q98Y5PyPAwAC",
        "outputId": "e9788966-be4b-480f-da49-676d013af4eb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "pathlib.PosixPath"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#　Unixのようなmagicコマンド　カレントディレクトリ表示(print working directory)\n",
        "%pwd"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "BmNcdPxZBHDx",
        "outputId": "aad2308e-a44f-4f54-f140-7797ad33b93f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'/content/drive/MyDrive'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# ファイル一覧の取得\n",
        "path = pathlib.Path.cwd()\n",
        "lis = [child for child in path.iterdir()]\n",
        "lis"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p5rBOtWuynxM",
        "outputId": "ae3bff3d-a60c-42f8-94e6-bbe089668b77"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[PosixPath('/content/.config'),\n",
              " PosixPath('/content/drive'),\n",
              " PosixPath('/content/sample_data')]"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Unixコマンド　リスト一覧の取得\n",
        "%ls"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VcLFI_0svx5f",
        "outputId": "bc0f14b3-ca62-4974-b79c-550b8bfb5bd8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " 160629復命書.docx\n",
            " 160629復命書.gdoc\n",
            " 20180423朝会（フリーアドレス）.gdoc\n",
            " \u001b[0m\u001b[01;34mappsheet\u001b[0m/\n",
            "\u001b[01;34m'Colab Notebooks'\u001b[0m/\n",
            " \u001b[01;34mColabNotebooks\u001b[0m/\n",
            " EBPMモデル構築事業.gsheet\n",
            "'Excel API.gsheet'\n",
            "'Gantt chart.gsheet'\n",
            " LIFE.gsheet\n",
            "'LINE Bot.gscript'\n",
            "'pzq-pscz-jyi - 2021年3月18日.gjam'\n",
            " Taro-ＨＰ改ざん報告.pdf\n",
            " Untitled0.ipynb\n",
            "'winmail (1).dat'\n",
            " winmail.dat\n",
            " お小遣い帳.gsheet\n",
            " ガントチャート.gsheet\n",
            " サウナ.gsheet\n",
            "\u001b[01;34m'フォームテスト (File responses)'\u001b[0m/\n",
            " フォームテスト.gform\n",
            " マーケットlog.gsheet\n",
            " \u001b[01;34m仕事\u001b[0m/\n",
            " 住民税決定通知書.gsheet\n",
            " ●修正後最終版【別紙１】R2業務実績等報告書.gdoc\n",
            " \u001b[01;34m個人\u001b[0m/\n",
            " 出産･産後準備リスト.gsheet\n",
            " 【別紙1】機能要件書.xlsx\n",
            "'【別紙2】データセンター機能要件書 (1).xlsx.gsheet'\n",
            " 【別紙2】データセンター機能要件書.xlsx.gsheet\n",
            " 家づくりメモ.gsheet\n",
            " 家庭菜園収穫量記録ノート.gsheet\n",
            " 家計簿2.gsheet\n",
            " 年末大掃除計画.gsheet\n",
            " \u001b[01;34m新しいフォルダー\u001b[0m/\n",
            " 【本編】インターネット環境分離システムの導入・運用保守業務委託仕様書.docx\n",
            " 氷熊真也様邸週間報告書３.gdoc\n",
            " 氷熊真也様邸週間報告書３.pdf\n",
            " 氷熊真也様邸週間報告書７.pdf\n",
            " 無題のサイト.gsite\n",
            " 無題のドキュメント.gdoc\n",
            " 無題のプレゼンテーション.gslides\n",
            " 統計データオープン化.gsheet\n",
            " 財務諸表.gsheet\n",
            " 資産運用.gsheet\n",
            "'長野駅周辺 駐車場.gmap'\n",
            "'音声 3.3gpp'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/drive/MyDrive"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EyEncOqs5pGw",
        "outputId": "2f58134c-3cb0-45de-e337-f6cad4c438fe"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/MyDrive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd ../"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HTHEGmWnDdMU",
        "outputId": "da36fcea-b0cf-48cb-fc77-55eacb5abc6f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd ./MyDrive"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "34AOd2QsDh-q",
        "outputId": "0a4db9ee-6fd1-4aaf-da97-939563a5cdee"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/MyDrive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# ファイル一覧の取得\n",
        "path = pathlib.Path.cwd()\n",
        "lis = [child for child in path.glob('*.pdf')] # 拡張子pdfファイルのみ取得\n",
        "lis"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-DcnCWP1y9bx",
        "outputId": "f53158bb-5517-4cb9-d96d-15dd76421523"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[PosixPath('/content/drive/MyDrive/Taro-ＨＰ改ざん報告.pdf'),\n",
              " PosixPath('/content/drive/MyDrive/氷熊真也様邸週間報告書３.pdf'),\n",
              " PosixPath('/content/drive/MyDrive/氷熊真也様邸週間報告書７.pdf')]"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os"
      ],
      "metadata": {
        "id": "sCX9h0X71jbl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "cdir = os.getcwd()\n",
        "print(cdir)\n",
        "type(cdir)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PrZEdb39BEFz",
        "outputId": "d631ffcf-4e6b-4594-cf94-2817a678fd11"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cdir = %pwd\n",
        "cdir"
      ],
      "metadata": {
        "id": "O7GXVhiA2M4l",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "outputId": "53291b40-b194-4737-ba01-2b6482de1231"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'/content'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "type(cdir)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i5QyO9Rq5AAR",
        "outputId": "abdc12c4-762a-48aa-8b17-4b95365198e0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# これは無理\n",
        "lis = %ls\n",
        "type(lis)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fwzumf-K4rgg",
        "outputId": "e846f04a-054e-4ff9-aa19-4016f3f4f29e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " 160629復命書.docx\n",
            " 160629復命書.gdoc\n",
            " 20180423朝会（フリーアドレス）.gdoc\n",
            " \u001b[0m\u001b[01;34mappsheet\u001b[0m/\n",
            "\u001b[01;34m'Colab Notebooks'\u001b[0m/\n",
            " \u001b[01;34mColabNotebooks\u001b[0m/\n",
            " EBPMモデル構築事業.gsheet\n",
            "'Excel API.gsheet'\n",
            "'Gantt chart.gsheet'\n",
            " LIFE.gsheet\n",
            "'LINE Bot.gscript'\n",
            "'pzq-pscz-jyi - 2021年3月18日.gjam'\n",
            " Taro-ＨＰ改ざん報告.pdf\n",
            " Untitled0.ipynb\n",
            "'winmail (1).dat'\n",
            " winmail.dat\n",
            " お小遣い帳.gsheet\n",
            " ガントチャート.gsheet\n",
            " サウナ.gsheet\n",
            "\u001b[01;34m'フォームテスト (File responses)'\u001b[0m/\n",
            " フォームテスト.gform\n",
            " マーケットlog.gsheet\n",
            " \u001b[01;34m仕事\u001b[0m/\n",
            " 住民税決定通知書.gsheet\n",
            " ●修正後最終版【別紙１】R2業務実績等報告書.gdoc\n",
            " \u001b[01;34m個人\u001b[0m/\n",
            " 出産･産後準備リスト.gsheet\n",
            " 【別紙1】機能要件書.xlsx\n",
            "'【別紙2】データセンター機能要件書 (1).xlsx.gsheet'\n",
            " 【別紙2】データセンター機能要件書.xlsx.gsheet\n",
            " 家づくりメモ.gsheet\n",
            " 家庭菜園収穫量記録ノート.gsheet\n",
            " 家計簿2.gsheet\n",
            " 年末大掃除計画.gsheet\n",
            " \u001b[01;34m新しいフォルダー\u001b[0m/\n",
            " 【本編】インターネット環境分離システムの導入・運用保守業務委託仕様書.docx\n",
            " 氷熊真也様邸週間報告書３.gdoc\n",
            " 氷熊真也様邸週間報告書３.pdf\n",
            " 氷熊真也様邸週間報告書７.pdf\n",
            " 無題のサイト.gsite\n",
            " 無題のドキュメント.gdoc\n",
            " 無題のプレゼンテーション.gslides\n",
            " 統計データオープン化.gsheet\n",
            " 財務諸表.gsheet\n",
            " 資産運用.gsheet\n",
            "'長野駅周辺 駐車場.gmap'\n",
            "'音声 3.3gpp'\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "NoneType"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# magicコマンドの一覧を表示\n",
        "%lsmagic"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 235
        },
        "id": "BczcQS644xeW",
        "outputId": "582ba637-02e8-4c18-8774-d66a84390f12"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Available line magics:\n",
              "%alias  %alias_magic  %autoawait  %autocall  %automagic  %autosave  %bookmark  %cat  %cd  %clear  %colors  %conda  %config  %connect_info  %cp  %debug  %dhist  %dirs  %doctest_mode  %ed  %edit  %env  %gui  %hist  %history  %killbgscripts  %ldir  %less  %lf  %lk  %ll  %load  %load_ext  %loadpy  %logoff  %logon  %logstart  %logstate  %logstop  %ls  %lsmagic  %lx  %macro  %magic  %man  %matplotlib  %mkdir  %more  %mv  %notebook  %page  %pastebin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %pip  %popd  %pprint  %precision  %prun  %psearch  %psource  %pushd  %pwd  %pycat  %pylab  %qtconsole  %quickref  %recall  %rehashx  %reload_ext  %rep  %rerun  %reset  %reset_selective  %rm  %rmdir  %run  %save  %sc  %set_env  %shell  %store  %sx  %system  %tb  %tensorflow_version  %time  %timeit  %unalias  %unload_ext  %who  %who_ls  %whos  %xdel  %xmode\n",
              "\n",
              "Available cell magics:\n",
              "%%!  %%HTML  %%SVG  %%bash  %%bigquery  %%capture  %%debug  %%file  %%html  %%javascript  %%js  %%latex  %%markdown  %%perl  %%prun  %%pypy  %%python  %%python2  %%python3  %%ruby  %%script  %%sh  %%shell  %%svg  %%sx  %%system  %%time  %%timeit  %%writefile\n",
              "\n",
              "Automagic is ON, % prefix IS NOT needed for line magics."
            ],
            "application/json": {
              "line": {
                "automagic": "AutoMagics",
                "autocall": "AutoMagics",
                "alias_magic": "BasicMagics",
                "lsmagic": "BasicMagics",
                "magic": "BasicMagics",
                "page": "BasicMagics",
                "pprint": "BasicMagics",
                "colors": "BasicMagics",
                "xmode": "BasicMagics",
                "quickref": "BasicMagics",
                "doctest_mode": "BasicMagics",
                "gui": "BasicMagics",
                "precision": "BasicMagics",
                "notebook": "BasicMagics",
                "save": "CodeMagics",
                "pastebin": "CodeMagics",
                "loadpy": "CodeMagics",
                "load": "CodeMagics",
                "edit": "KernelMagics",
                "config": "ConfigMagics",
                "prun": "ExecutionMagics",
                "pdb": "ExecutionMagics",
                "debug": "ExecutionMagics",
                "tb": "ExecutionMagics",
                "run": "ExecutionMagics",
                "timeit": "ExecutionMagics",
                "time": "ExecutionMagics",
                "macro": "ExecutionMagics",
                "load_ext": "ExtensionMagics",
                "unload_ext": "ExtensionMagics",
                "reload_ext": "ExtensionMagics",
                "history": "HistoryMagics",
                "recall": "HistoryMagics",
                "rerun": "HistoryMagics",
                "logstart": "LoggingMagics",
                "logstop": "LoggingMagics",
                "logoff": "LoggingMagics",
                "logon": "LoggingMagics",
                "logstate": "LoggingMagics",
                "pinfo": "NamespaceMagics",
                "pinfo2": "NamespaceMagics",
                "pdef": "NamespaceMagics",
                "pdoc": "NamespaceMagics",
                "psource": "NamespaceMagics",
                "pfile": "NamespaceMagics",
                "psearch": "NamespaceMagics",
                "who_ls": "NamespaceMagics",
                "who": "NamespaceMagics",
                "whos": "NamespaceMagics",
                "reset": "NamespaceMagics",
                "reset_selective": "NamespaceMagics",
                "xdel": "NamespaceMagics",
                "alias": "OSMagics",
                "unalias": "OSMagics",
                "rehashx": "OSMagics",
                "pwd": "OSMagics",
                "cd": "OSMagics",
                "env": "OSMagics",
                "set_env": "OSMagics",
                "pushd": "OSMagics",
                "popd": "OSMagics",
                "dirs": "OSMagics",
                "dhist": "OSMagics",
                "sc": "OSMagics",
                "sx": "OSMagics",
                "system": "OSMagics",
                "bookmark": "OSMagics",
                "pycat": "OSMagics",
                "pip": "Other",
                "conda": "PackagingMagics",
                "matplotlib": "PylabMagics",
                "pylab": "PylabMagics",
                "killbgscripts": "ScriptMagics",
                "autoawait": "AsyncMagics",
                "ed": "Other",
                "hist": "Other",
                "rep": "Other",
                "clear": "KernelMagics",
                "less": "KernelMagics",
                "more": "KernelMagics",
                "man": "KernelMagics",
                "connect_info": "KernelMagics",
                "qtconsole": "KernelMagics",
                "autosave": "KernelMagics",
                "mkdir": "Other",
                "rmdir": "Other",
                "mv": "Other",
                "rm": "Other",
                "cp": "Other",
                "cat": "Other",
                "ls": "Other",
                "ll": "Other",
                "lf": "Other",
                "lk": "Other",
                "ldir": "Other",
                "lx": "Other",
                "store": "StoreMagics",
                "shell": "Other",
                "tensorflow_version": "Other"
              },
              "cell": {
                "js": "DisplayMagics",
                "javascript": "DisplayMagics",
                "latex": "DisplayMagics",
                "svg": "DisplayMagics",
                "html": "DisplayMagics",
                "markdown": "DisplayMagics",
                "prun": "ExecutionMagics",
                "debug": "ExecutionMagics",
                "timeit": "ExecutionMagics",
                "time": "ExecutionMagics",
                "capture": "ExecutionMagics",
                "sx": "OSMagics",
                "system": "OSMagics",
                "!": "OSMagics",
                "writefile": "OSMagics",
                "script": "ScriptMagics",
                "sh": "Other",
                "bash": "Other",
                "perl": "Other",
                "ruby": "Other",
                "python": "Other",
                "python2": "Other",
                "python3": "Other",
                "pypy": "Other",
                "SVG": "Other",
                "HTML": "Other",
                "file": "Other",
                "bigquery": "Other",
                "shell": "Other"
              }
            }
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "from glob import glob\n",
        "\n",
        "# print(\"C://root\")\n",
        "for i in glob(\"/content/drive/MyDrive/仕事/病院機構/**\", recursive=True):\n",
        "    indent = \"  \" * (i.count(os.sep))\n",
        "    print(indent + os.path.basename(i))"
      ],
      "metadata": {
        "id": "xJ_G_cpL41pU",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9595b1cf-96bd-4d9c-9608-24269b916b93"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "            \n",
            "            病院事業・介護事業サービス.zip\n",
            "            経営状況表３０年度.zip\n",
            "            財務諸表（説明用　コメントあり）.zip\n",
            "            試算表（H30年度）.zip\n",
            "            試算表ほか.zip\n",
            "            決算概要書(全体・税込).zip\n",
            "            テスト用（税込）様式１  決算概要　様式３収支総括・内訳表（01信州）.xlsm\n",
            "            年間スケジュール.xlsx\n",
            "            新しいフォルダー\n",
            "              【０６月】経営状況表04木曽.xlsx\n",
            "              【０６月】経営状況表00本部.xlsx\n",
            "              【０６月】経営状況表02駒ヶ根.xlsx\n",
            "              【０６月】経営状況表05こども.xlsx\n",
            "              【０６月】経営状況表03阿南.xlsx\n",
            "              【０６月】経営状況表01信州.xlsx\n",
            "              【０６月】経営状況表00全体（パスワードあり）.xlsx\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "jwyRBTG-5kuR"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}