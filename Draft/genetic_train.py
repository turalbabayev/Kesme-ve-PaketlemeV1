import matplotlib.pyplot as plt
import random
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.x = -1
        self.y = -1  # Sığmayan çemberlerin koordinatları (-1, -1)

class Bin:
    def __init__(self, width, height):
        self.width = width  # Yerleştirilecek alanın genişliği
        self.height = height  # Yerleştirilecek alanın uzunluğu
        self.circles = []  # Yerleştirilecek alandaki çemberlerin tutulduğu liste
        self.fitness = 0  # Yerleştirilen çemberlerin alanının toplamı

    def add_circle(self, circle):  # Çember Ekleme Fonksiyonu
        self.circles.append(circle)  # Çemberleri tutan listeye gelen uygun çemberi ekleme işlemi
        self.fitness += math.pi * circle.radius**2  # Yerleştirilen çemberin alanını fitness değerine ekleme işlemi

def is_valid_location(bin, circle, x, y):  # Uygun Yer Bulma Fonksiyonu
    if x + 2 * circle.radius > bin.width or y + 2 * circle.radius > bin.height:
        return False
    for c in bin.circles:
        if math.sqrt((x - c.x)**2 + (y - c.y)**2) < circle.radius + c.radius:
            return False
    return True

def pack_circles(circles, bin_width, bin_height):
    bins = [Bin(bin_width, bin_height)]

    for circle in circles:
        fitted = False
        for bin in bins:
            for y in range(bin.height):
                for x in range(bin.width):
                    if is_valid_location(bin, circle, x, y):
                        circle.x = x + circle.radius
                        circle.y = y + circle.radius
                        bin.add_circle(circle)
                        fitted = True
                        break
                if fitted:
                    break
            if fitted:
                break

    return bins

def visualize_packing(bins):
    plt.figure()
    colors = ['#FF5733', '#33FF57', '#5733FF', '#FF57D5', '#33A6FF', "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FFA500", "#FFC0CB", "#800080", "#40E0D0", "#808080", "#A52A2A", "#FFD700", "#E6E6FA"]

    for i, bin in enumerate(bins):
        plt.subplot(1, len(bins), i + 1)
        plt.title(f'Bin {i + 1}')
        for j, circle in enumerate(bin.circles):
            color = colors[j % len(colors)]
            plt.gca().add_patch(plt.Circle((circle.x, circle.y), circle.radius, fill=True, color=color, alpha=0.7))

        for x in range(bin.width):
            for y in range(bin.height):
                is_empty = True
                for circle in bin.circles:
                    if math.sqrt((x - circle.x)**2 + (y - circle.y)**2) < circle.radius:
                        is_empty = False
                        break
                if is_empty:
                    plt.gca().add_patch(plt.Rectangle((x, y), 1, 1, fill=True, color='black'))  # Boş alanları siyahla boyar

        plt.xlim(0, bin.width)
        plt.ylim(0, bin.height)

    plt.show()

# Geri kalan kısım dikdörtgenlerin yerine çemberler için olan kısmı içermektedir.

def create_chromosome(circles):
    chromosome = []
    for i in range(len(circles)):
        chromosome.append(i)  # Çemberlerin sıralamasını kromozoma ekleme işlemi
        random.shuffle(chromosome)  # Çemberlerin sıralamasını rastgele karıştırma işlemi
    return chromosome

def decode_chromosome(chromosome, circles):
    decoded_circles = []
    for i in range(len(circles) if circles else 0):
        index = chromosome[i] if chromosome and i < len(chromosome) else 0
        circle = Circle(circles[index].radius)
        decoded_circles.append(circle)
    return decoded_circles



def evaluate_population(population, circles, bin_width, bin_height):
    evaluated_population = []
    for chromosome in population:
        decoded_circles = decode_chromosome(chromosome, circles)
        bins = pack_circles(decoded_circles, bin_width, bin_height)
        fitness = bins[0].fitness
        evaluated_population.append((chromosome, fitness))
    return evaluated_population

def select_population(evaluated_population, population_size):
    selected_population = []
    total_fitness = sum(fitness for chromosome, fitness in evaluated_population)
    probabilities = [fitness / total_fitness for chromosome, fitness in evaluated_population]
    for i in range(population_size):
        r = random.random()
        s = 0
        for j in range(len(evaluated_population)):
            s += probabilities[j]
            if r < s:
                selected_population.append(evaluated_population[j][0])
                break
    return selected_population

def crossover_population(population, crossover_rate):
    crossed_population = []
    for i in range(0, len(population), 2):
        parent1 = population[i]
        parent2 = population[i + 1]
        child1 = parent1.copy()
        child2 = parent2.copy()
        r = random.random()
        if r < crossover_rate:
            point = random.randint(1, len(parent1) - 1)
            child1[:point] = parent2[:point]
            child2[:point] = parent1[:point]
        crossed_population.append(child1)
        crossed_population.append(child2)
    return crossed_population

def mutate_population(population, mutation_rate):
    mutated_population = []
    for chromosome in population:
        mutated_chromosome = chromosome.copy()
        r = random.random()
        if r < mutation_rate:
            point = random.randint(0, len(chromosome) - 1)
            if point < len(chromosome) // 2:
                swap = random.randint(0, len(chromosome) // 2 - 1)
                mutated_chromosome[point], mutated_chromosome[swap] = mutated_chromosome[swap], mutated_chromosome[point]
            else:
                mutated_chromosome[point] = 1 - mutated_chromosome[point]
        mutated_population.append(mutated_chromosome)
    return mutated_population
def create_population(circles, population_size):
    population = []
    for i in range(population_size):
        chromosome = create_chromosome(circles)
        population.append(chromosome)
    return population

def genetic_algorithm(circles, bin_width, bin_height, population_size, iteration, crossover_rate, mutation_rate):
    population = create_population(circles, population_size)
    best_chromosome = None
    best_fitness = 0
    for i in range(1, iteration):  # İlk iterasyonda popülasyonu değerlendirmiyoruz, bu yüzden 1'den başlatıyoruz.
        evaluated_population = evaluate_population(population, circles, bin_width, bin_height)
        for chromosome, fitness in evaluated_population:
            if fitness > best_fitness:
                best_chromosome = chromosome
                best_fitness = fitness
        selected_population = select_population(evaluated_population, population_size)
        crossed_population = crossover_population(selected_population, crossover_rate)
        mutated_population = mutate_population(crossed_population, mutation_rate)
        population = mutated_population

        print(f"Iterasyon {i} - En iyi fitness: {best_fitness}")
    print("En iyi kromozom:", best_chromosome)
    print("En iyi fitness değeri:", best_fitness)
    return best_chromosome, best_fitness


if __name__ == "__main__":
    circles = []
    with open("Data/circle_data.txt", "r") as file:
        num_circles = int(file.readline().strip())
        bin_width, bin_height = map(int, file.readline().strip().split())

        for _ in range(num_circles):
            radius = int(file.readline().strip())
            circles.append(Circle(radius))

    # GA parametreleri
    population_size = 2  # Popülasyon boyutu
    iteration = 1  # Iterasyon sayısı
    crossover_rate = 0.8  # Çaprazlama oranı
    mutation_rate = 0.1  # Mutasyon oranı

    best_chromosome, best_fitness = genetic_algorithm(circles, bin_width, bin_height, population_size, iteration, crossover_rate, mutation_rate)  # Genetik algoritmayı çalıştırma işlemi
    best_circles = decode_chromosome(best_chromosome, circles)  # En iyi kromozomu çembere dönüştürme işlemi
    best_bins = pack_circles(best_circles, bin_width, bin_height)  # En iyi çemberleri yerleştirme işlemi

    total_circles_area = sum(math.pi * circle.radius**2 for circle in circles)
    print(total_circles_area)
    total_packing_area = bin_width * bin_height
    print(total_packing_area)
    total_fitted_area = sum(math.pi * circle.radius**2 for bin in best_bins for circle in bin.circles)
    success_rate = (total_fitted_area / total_circles_area) * 100
    plt.suptitle(f'C2_1 Datası \nBaşarı Oranı: {success_rate}%', fontsize=14)
    visualize_packing(best_bins)  # Yerleştirme sonucunu görselleştirme işlemi
