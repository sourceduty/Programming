# Example 3D Radar GUI 2
# Simulated Pulse-Doppler Radar

import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
import threading
import time

class RadarSimulator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.running = False

    def initUI(self):
        self.setWindowTitle("Pulse-Doppler Radar Simulation (3D)")
        self.setGeometry(100, 100, 800, 600)
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        self.canvas = FigureCanvas(plt.figure())
        layout.addWidget(self.canvas)
        
        self.start_button = QPushButton("Start Simulation")
        self.start_button.clicked.connect(self.start_simulation)
        layout.addWidget(self.start_button)
        
        self.stop_button = QPushButton("Stop Simulation")
        self.stop_button.clicked.connect(self.stop_simulation)
        layout.addWidget(self.stop_button)

    def start_simulation(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.run_simulation, daemon=True)
            self.thread.start()

    def stop_simulation(self):
        self.running = False

    def run_simulation(self):
        while self.running:
            range_doppler_data = self.generate_pulse_doppler()
            self.update_plot(range_doppler_data)
            time.sleep(0.1)  # Simulate real-time update

    def generate_pulse_doppler(self):
        # Simulated Pulse-Doppler Radar Data
        num_ranges = 128
        num_doppler_bins = 128
        
        radar_signal = np.random.randn(num_ranges, num_doppler_bins) + 1j * np.random.randn(num_ranges, num_doppler_bins)
        doppler_fft = np.fft.fftshift(np.fft.fft2(radar_signal))
        magnitude = 20 * np.log10(np.abs(doppler_fft) + 1e-6)
        return magnitude

    def update_plot(self, data):
        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111, projection='3d')
        X, Y = np.meshgrid(np.linspace(-64, 64, data.shape[1]), np.linspace(0, 128, data.shape[0]))
        ax.plot_surface(X, Y, data, cmap='jet')
        ax.set_xlabel("Doppler Frequency")
        ax.set_ylabel("Range")
        ax.set_zlabel("Magnitude (dB)")
        ax.set_title("Real-time 3D Range-Doppler Map")
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication([])
    radar_sim = RadarSimulator()
    radar_sim.show()
    app.exec_()
