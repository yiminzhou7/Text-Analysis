import matplotlib.pyplot as plt


def count_figures(xml):
    """
    Counts the number of figure elements in the provided XML document.

    INPUT:
    - xml (BeautifulSoup): The XML document parsed using BeautifulSoup.

    OUTPUT:
    - Number of figure elements found in the XML document.
    """

    # Verify that grobid_results is not empty
    if not xml:
        return None
    else:
        # Find all <figure> elements within the XML document
        figures = xml.find_all('figure')
        return len(figures)


def histogram(fig_count, output_path):
    """
    Draw a histogram of the number of figures per article and save it as a PNG file.

    INPUT:
    - fig_count (list): List of number of figures per article.
    - output_path (str): Path where the histogram PNG file will be saved.
    """
    article_indices = list(range(1, len(fig_count) + 1))  # Indices representing the articles
    plt.figure(figsize=(10, 6))
    plt.bar(article_indices, fig_count, color='blue')
    plt.xticks(article_indices)
    plt.xlabel('Article')
    plt.ylabel('Number of Figures')
    plt.title('Histogram of Number of Figures per Article')
    plt.grid(True)
    plt.savefig(output_path)
    print(f"Histogram saved as {output_path}")