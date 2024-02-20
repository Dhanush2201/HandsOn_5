import heapq as hq

class CustomHeap:
    def __init__(self):
        self.custom_heap = []

    def initialize_custom_heap(self, elements):
        self.custom_heap = elements
        hq.heapify(self.custom_heap)

    def extract_custom_min(self):
        if not self.custom_heap:
            return None
        return hq.heappop(self.custom_heap)

    def insert_custom_element(self, value):
        hq.heappush(self.custom_heap, value)

    def display_custom_heap(self):
        print("Custom Heap:", self.custom_heap)

if __name__ == "__main__":
    custom_heap_instance = CustomHeap()

    while True:
        print("\nChoose an option:")
        print("1. Initialize custom heap")
        print("2. Insert custom element")
        print("3. Extract minimum custom element")
        print("4. Display custom heap")
        print("5. Exit")

        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            user_input_elements = input("Enter space-separated elements to initialize custom heap: ").split()
            custom_heap_instance.initialize_custom_heap(user_input_elements)
        elif user_choice == '2':
            user_input_value = input("Enter element to insert into custom heap: ")
            custom_heap_instance.insert_custom_element(user_input_value)
        elif user_choice == '3':
            extracted_min = custom_heap_instance.extract_custom_min()
            if extracted_min is not None:
                print("Extracted minimum custom element:", extracted_min)
            else:
                print("Custom heap is empty.")
        elif user_choice == '4':
            custom_heap_instance.display_custom_heap()
        elif user_choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
