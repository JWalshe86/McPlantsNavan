<form class="form" action="{% url 'add_to_bag' product.id %}" method="POST">
                        {% csrf_token %}
                        <div class="form-row">
                            {% with product.has_sizes as s %}
                            {% if s %}
                                <div class="col-12">
                                    <p><strong>Size:</strong></p>
                                    <select class="form-control rounded-0 w-50" name="product_size" id='id_product_size'>
                                        <option value="xs">XS</option>
                                        <option value="s">S</option>
                                        <option value="m" selected>M</option>
                                        <option value="l">L</option>
                                        <option value="xl">XL</option>
                                    </select>
                                </div>
                            {% endif %}
                            <div class="col{% if s %}-12 mt-2{% endif %}">
                                <a href="{% url 'products' %}" class="btn btn-outline-black rounded-0 mt-5">
                                    <span class="icon">
                                        <i class="fas fa-chevron-left"></i>
                                    </span>
                                    <span class="text-uppercase">Keep Shopping</span>
                                </a>
                                <input type="submit" class="btn btn-black rounded-0 text-uppercase mt-5" value="Add to Bag">
                            </div>
                            <input type="hidden" name="redirect_url" value="{{ request.path }}">
                            {% endwith %}
                        </div>
                    </form>
