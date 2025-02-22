import streamlit as st
import nbformat
import base64
import io
def display_notebook_charts(notebook_path):
    """
    Extracts and displays interactive charts and markdown from an IPython notebook.
    Supports both Plotly and Matplotlib outputs.
    """
    with open(notebook_path, 'r') as f:
        nb = nbformat.read(f, as_version=4)

    code_cell_count = 0
    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            st.markdown(cell.source)
        elif cell.cell_type == 'code':
            if code_cell_count < 2:
                code_cell_count += 1
                continue
            # Display cell source if needed
            st.code(cell.source, language="python")
            for output in cell.outputs:
                if output.output_type in ['display_data', 'execute_result']:
                    if 'image/png' in output.data:
                        try:
                            # Decode the PNG image and display it with Streamlit
                            image_data = base64.b64decode(output.data['image/png'])
                            st.image(image_data, use_column_width=True)
                        except Exception as e:
                            st.error(f"Error displaying Matplotlib plot: {e}")
                    elif 'text/plain' in output.data:
                        st.text(output.data['text/plain'])
                elif output.output_type == 'stream':
                    st.text(output.get('text', ''))
                elif output.output_type == 'error':
                    st.error("\n".join(output.get('traceback', [])))
