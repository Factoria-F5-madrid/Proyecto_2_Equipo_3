// Create: /home/hoodche/F5/Proyecto_2_Equipo_3/Food5/food5-frontend/src/services/api.js

const API_BASE_URL = 'http://localhost:8000';

class ApiService {
  async request(method, endpoint, data = null) {
    const config = {
      method,
      headers: {
        'Content-Type': 'application/json',
      },
    };

    if (data) {
      config.body = JSON.stringify(data);
    }

    try {
      const response = await fetch(`${API_BASE_URL}${endpoint}`, config);
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      console.error('API Request failed:', error);
      throw error;
    }
  }

  // Menu items
  async getMenus() {
    return this.request('GET', '/menu/');
  }

  async createMenu(menuData) {
    return this.request('POST', '/menu/', menuData);
  }

  // Drinks
  async getDrinks() {
    return this.request('GET', '/drinks/');
  }

  async createDrink(drinkData) {
    return this.request('POST', '/drinks/', drinkData);
  }

  // Bread
  async getBread() {
    return this.request('GET', '/bread/');
  }

  // First Course
  async getFirstCourses() {
    return this.request('GET', '/first_course/');
  }

  // Second Course
  async getSecondCourses() {
    return this.request('GET', '/second_course/');
  }

  // Desserts
  async getDesserts() {
    return this.request('GET', '/dessert/');
  }

  // Customers
  async getCustomers() {
    return this.request('GET', '/customer/');
  }

  async createCustomer(customerData) {
    return this.request('POST', '/customer/', customerData);
  }

  // Orders
  async getOrders() {
    return this.request('GET', '/order/');
  }

  async createOrder(orderData) {
    return this.request('POST', '/order/', orderData);
  }
}

export const api = new ApiService();
export default api;