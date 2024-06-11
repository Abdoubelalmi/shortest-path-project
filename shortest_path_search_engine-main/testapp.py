import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ShortestPathFinder(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shortest Path Finder")
        self.geometry("400x400")

        self.graph = None
        self.create_widgets()

    def create_widgets(self):
        frame_input = ttk.Frame(self, padding="10")
        frame_input.pack(fill='both', expand=True)

        frame_buttons = ttk.Frame(self, padding="10")
        frame_buttons.pack(fill='x')

        ttk.Label(frame_input, text="Select City:").pack(side='left', padx=5, pady=5)

        cities = ["Adrar", "Ain Defla", "Ain Temouchent", "Alger", "Annaba", "Batna",
                  "Bechar", "Bejaia", "Biskra", "Blida", "Bordj Bou Arreridj", "Bouira",
                  "Boumerdes", "Chlef", "Constantine", "Djelfa", "El Bayadh", "El Oued",
                  "El Tarf", "Ghardaia", "Guelma", "Illizi", "Jijel", "Khenchela",
                  "Laghouat", "Muaskar", "Medea", "Mila", "Mostaganem", "Msila", "Naama",
                  "Oran", "Ouargla", "Oum el Bouaghi", "Relizane", "Saida", "Setif", "Sidi Bel Abbes",
                  "Skikda", "Souk Ahras", "Tamanrasset", "Tebessa", "Tiaret", "Tindouf",
                  "Tipaza", "Tissemsilt", "Tizi Ouzou", "Tlemcen"]

        self.combobox_city = ttk.Combobox(frame_input, values=cities)
        self.combobox_city.pack(side='left', padx=5, pady=5)
        self.combobox_city.bind("<<ComboboxSelected>>", self.update_nodes)

        ttk.Label(frame_input, text="Source Place:").pack(side='left', padx=5, pady=5)
        self.listbox_source = tk.Listbox(frame_input, selectmode="browse")
        self.listbox_source.pack(side='left', fill='both', expand=True, padx=5, pady=5)

        ttk.Label(frame_input, text="Destination Place:").pack(side='left', padx=5, pady=5)
        self.listbox_target = tk.Listbox(frame_input, selectmode="browse")
        self.listbox_target.pack(side='left', fill='both', expand=True, padx=5, pady=5)

        ttk.Button(frame_buttons, text="Find Shortest Path", command=self.find_shortest_path).pack(fill='x', padx=5, pady=5)

    def get_map_data(self, city_name):
        place_name = f"{city_name}, Algeria"
        self.graph = ox.graph_from_place(place_name, network_type='drive')

    def update_nodes(self, event=None):
        selected_city = self.combobox_city.get()
        self.get_map_data(selected_city)
        self.listbox_source.delete(0, tk.END)
        self.listbox_target.delete(0, tk.END)
        node_names = self.get_node_names(self.graph)
        for node in node_names:
            self.listbox_source.insert(tk.END, node)
            self.listbox_target.insert(tk.END, node)

    def get_node_names(self, graph):
        return {node: graph.nodes[node].get('name', f"Unnamed Node {node}") for node in graph.nodes()}

    def a_star_search(self, graph, source, target):
        return nx.astar_path(graph, source, target, weight='length')

    def plot_shortest_path(self, graph, shortest_path):
        fig, ax = ox.plot_graph_route(graph, shortest_path, route_color='g', route_linewidth=3, node_size=0, figsize=(15, 15), show=False, close=False)
        plt.tight_layout()
        plt.axis('off')
        plt.show(block=False)

    def find_shortest_path(self):
        selected_source = self.listbox_source.get(tk.ACTIVE)
        selected_target = self.listbox_target.get(tk.ACTIVE)
        
        if selected_source and selected_target:
            shortest_path = self.a_star_search(self.graph, selected_source, selected_target)
            self.plot_shortest_path(self.graph, shortest_path)
        else:
            messagebox.showwarning("Warning", "Please select both source and target nodes.")

if __name__ == "__main__":
    app = ShortestPathFinder()
    app.mainloop()
